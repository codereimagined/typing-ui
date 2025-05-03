<script>
  export let targetText = '';
  export let typedText = '';

  function getStyle(char, i) {
    if (i >= typedText.length) {
      return ''
    }
    return typedText[i] === char ? 'correct' : 'incorrect'
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
    width: 800px;
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
</style>
