<script lang="ts">
  export let targetText = '';
  export let typedText = '';
  export let fixIndexes = new Set<number>();

  function getStyle(char: string, i: number) {
    let correctOrFix = fixIndexes.has(i) ? 'fixed' : 'correct';
    if (i >= typedText.length) {
      return ''
    }
    let typedChar = typedText[i];
    if (typedChar === char) { return correctOrFix }
    return /\s/.test(typedChar) && /\s/.test(char) ? correctOrFix : 'incorrect';
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
    color: black;
  }
  .highlighted-text .fixed {
    font-weight: bold;
    color: black;
    background-color: lightgray;
  }
  .highlighted-text .incorrect {
    color: black;
    font-weight: bold;
    background-color: red;
  }
</style>
