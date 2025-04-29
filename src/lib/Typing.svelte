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
    return typedText[i] == char ? 'correct' : 'incorrect'
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
  width: 600px;
  margin: 2rem auto;
}

.highlighted-text {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  padding: 0.5rem;
  font-size: 1.2rem;
  white-space: pre;
  pointer-events: none;
  color: #aaa;
}

.highlighted-text .correct {
  color: black;
  font-weight: bold;
}

.highlighted-text .incorrect {
  background-color: red;
  font-weight: bold;
}

.typing-input {
  width: 100%;
  padding: 0.5rem;
  font-size: 1.2rem;
  background: transparent;
  color: transparent;
  outline: none;
  caret-color: transparent;
  resize: none;
  overflow: hidden;
  border: none;
}
</style>
