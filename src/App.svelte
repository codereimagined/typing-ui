<script lang="ts">
  import Typing from './lib/Typing.svelte'

  const text = [
    "a quick brown fox jumped over the brown dog",
    "type something from outside...",
    "more typing of cool text",
    "the story of Oliver continus...",
    "end of the story!"
  ];
  let index = 0;
  function focusNext() {
    if (index < text.length) {
      index += 1;
      return text[index - 1];
    } else {
      alert("The end of the lesson");
    }
  }

  function focusPrev() {
    if (index > 0) {
      index -= 1;
      return text[index - 1];
    } else {
      alert("The beginning of the lesson");
    }
  }
</script>

<main>
  {#each text.slice(0, index - 1) as item}
    <p>{item}</p>
  {/each}
  <div class="card">
    <Typing onFinish={focusNext} onBackspace={focusPrev} />
  </div>
  {#each text.slice(index) as item}
    <p>{item}</p>
  {/each}
</main>

<style>
</style>
