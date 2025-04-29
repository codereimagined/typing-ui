<script>
  let targetText = 'the quick brown fox jumps over the lazy dog';
  let typedText = '';

  function handleInput(e) {
    typedText = e.target.value;
  }

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
  
  <textarea
    bind:value={typedText}
    on:input={handleInput}
    class="typing-input"
    spellcheck="false"
    autofocus
    rows="1"
  ></textarea>
</div>

<style>
  .typing-container {
    position: relative;
    width: 800px;
    margin: 50px auto;
    font-size: 28px;
    font-family: monospace;
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
    width: 100%;
    border: none;
    background: transparent;
    color: transparent;
    font-size: 28px;
    font-family: monospace;
    white-space: pre-wrap;
    word-wrap: break-word;
    outline: none;
    caret-color: transparent; /* hide carret */
    resize: none;
  }
</style>
