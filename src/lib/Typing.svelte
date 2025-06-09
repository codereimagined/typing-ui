<script lang="ts">
  import { message, pastMessages } from './sharedStore';
  export let switchNext = () =>  {};
  export let switchPrevious = () =>  {};
  export let targetText = '';
  export let typedText = '';
  export let fixIndexes = new Set<number>();

  let hitMissTime: { value: boolean; time: number }[] = [];
  let textAreaElement: HTMLTextAreaElement;

  function handleInput(e: InputEvent) {
    typedText = (e.target as HTMLTextAreaElement)?.value;
    if (typedText.length === targetText.length) {
      switchNext();
      textAreaElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
    if (e.inputType !== 'deleteContentBackward') {
      appendHitMissTime();
    } else {
      // Delete the last correctly typed character on Backspace
      const index = hitMissTime.findIndex(obj => obj.value === true);
      if (index !== -1) {
        hitMissTime.splice(index, 1);
      }
    }
  }

  function appendHitMissTime() {
    let typedCharPosition = typedText.length - 1;
    let hitOrMiss = typedText[typedCharPosition] === targetText[typedCharPosition];
    if (!hitOrMiss) {
      fixIndexes.add(typedCharPosition);
    }
    let currentTime = new Date().getTime();
    let lastKeyTime = hitMissTime.at(-1)?.time || 0;
    if (currentTime - lastKeyTime > 5000) {
      if (hitMissTime.length > 10) {
        pastMessages.update(arr => [getStatusMessage(hitMissTime, lastKeyTime), ...arr.slice(0, 10)]);
      }
      message.set("Keep typing to know your speed and accuracy!");
      hitMissTime = [];
    }
    hitMissTime.push({value: hitOrMiss, time: currentTime});

    if (hitMissTime.length % 10 === 9) {
      message.set(getStatusMessage(hitMissTime));
    }
  }

  function getStatusMessage(hitMissTime: {value: boolean, time: number}[], currentTime?: number) {
    // Compute speed and accuracy message
    if (hitMissTime.length === 0) { return '' }
    if (!currentTime) { currentTime = new Date().getTime() }
    let startTime = hitMissTime[0].time;
    let correctCount = hitMissTime.filter(x => x.value).length;
    let totalCount = hitMissTime.length;
    let speedCharsPerMin = totalCount / (currentTime - startTime) * 1000 * 60;
    let speedWordsPerMin = speedCharsPerMin / 5; // divide the average word length for English
    return `Speed: ${speedWordsPerMin.toFixed(2)} words/min, accuracy: ${(correctCount/totalCount).toFixed(2)}, streak: ${totalCount}`;
  }

  function handleKeyDown(e: KeyboardEvent) {
    // Handle backspace needs to be in "on:keydown" as "on:input" won't trigger if textarea is empty
    if (e.key === 'Backspace' && typedText.length === 0) {
      switchPrevious();
      textAreaElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }

  function getStyle(char: string, i: number) {
    let correctOrFix = fixIndexes.has(i) ? 'fixed' : 'correct';
    if (i >= typedText.length) {
      return ''
    }
    let typedChar = typedText[i];
    if (typedChar === char) { return correctOrFix }
    return /\s/.test(typedChar) && /\s/.test(char) ? correctOrFix : 'incorrect';
  }

  function keepFocus() {
    setTimeout(() => {
      // Only allowing to focus on Chapter selection
      const selectedElement = document.activeElement?.tagName;
      if (selectedElement === 'SELECT') {
        return;
      }
      textAreaElement?.focus();
    }, 0);
  }
</script>

<div class="typing-container">
  <div class="highlighted-text">
    {#each targetText.split('') as char, i}
      <span class={getStyle(char, i)}>
        {char}
      </span>
    {/each}
  </div>
  
  <textarea
    bind:this={textAreaElement}
    bind:value={typedText}
    on:input={handleInput}
    on:keydown={handleKeyDown}
    on:mousedown|preventDefault
    on:mouseup|preventDefault
    on:click|preventDefault
    on:mousemove|preventDefault
    on:selectstart|preventDefault
    on:blur={keepFocus}
    class="typing-input"
    spellcheck="false"
    autofocus
    rows="1"
  ></textarea>
</div>

<style>
  .typing-container {
    position: relative;
    width: 1200px;
    margin: .5em auto;
    font-size: 24px;
    font-family: monospace;
    padding: .5em;
  }
  .highlighted-text {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    pointer-events: none; /* Allows clicking through to input */
    color: gray;
    white-space: pre-wrap;
    word-wrap: break-word;
    text-align: left;
  }
  .highlighted-text .correct {
    font-weight: bold;
    color: var(--type-color);
  }
  .highlighted-text .fixed {
    font-weight: bold;
    color: var(--type-color);
    background-color: var(--fixed-bg-color);
  }
  .highlighted-text .incorrect {
    color: var(--type-color);
    font-weight: bold;
    background-color: red;
  }
  .typing-input {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    width: 100%;
    border: none;
    background: transparent;
    color: transparent;
    font-size: 24px;
    font-family: monospace;
    white-space: pre-wrap;
    word-wrap: break-word;
    outline: none;
    resize: none;
    caret-color: var(--caret-color);
  }
</style>
