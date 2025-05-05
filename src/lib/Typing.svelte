<script lang="ts">
  export let switchNext = () =>  {};
  export let switchPrevious = () =>  {};
  export let targetText = '';
  export let typedText = '';
  let textAreaElement: HTMLTextAreaElement;

  function handleInput(e: Event) {
      typedText = (e.target as HTMLTextAreaElement)?.value;
      if (typedText.length === targetText.length) {
        switchNext();
        textAreaElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }

  function handleKeyDown(e: KeyboardEvent) {
      // Handle backspace needs to be in "on:keydown" as "on:input" won't trigger if textarea is empty
      if (e.key === 'Backspace' && typedText.length === 0) {
        switchPrevious();
        textAreaElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
  }

  function getStyle(char: string, i: number) {
      if (i >= typedText.length) {
          return ''
      }
      let typedChar = typedText[i];
      if (typedChar === char) { return 'correct' }
      return /\s/.test(typedChar) && /\s/.test(char) ? 'correct' : 'incorrect';
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
    font-size: 28px;
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
    color: black;
  }
  .highlighted-text .incorrect {
    color: black;
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
    font-size: 28px;
    font-family: monospace;
    white-space: pre-wrap;
    word-wrap: break-word;
    outline: none;
    caret-color: black;
    resize: none;
  }
</style>
