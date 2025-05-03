<script>
  export let onFinish;
  export let onBackspace;
  export let targetText;
  export let typedText;

  function handleInput(e) {
    if (e.inputType  === 'deleteContentBackward' && typedText.length === 0) {
      onBackspace();
      return; // Prevent backspace from deleting text in the previous input
    }
    typedText = e.target.value;
    if (typedText.length === targetText.length) {
      onFinish();
    }
  }

  function getStyle(char, i) {
    if (i >= typedText.length) {
      return ''
    }
    return typedText[i] === char ? 'correct' : 'incorrect'
  }

  function keepFocus() {
    setTimeout(() => {
      document.getElementsByClassName('typing-input')[0]?.focus();
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
    bind:value={typedText}
    on:input={handleInput}
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
