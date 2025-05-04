<script lang="ts">
  import Typing from './lib/Typing.svelte'
  import ReadOnly from './lib/ReadOnly.svelte'

  const text = [
    { target: "a quick brown fox jumped over the lazy dog ", typed: "" },
    { target: "type something from outside... ", typed: "" },
    { target: "more typing of cool text ", typed: "" },
    { target: "the story of Oliver continues... ", typed: ""},
    { target: "end of the story!", typed: "" }
  ];
  let index = 0;

  function focusNext() {
    if (index < text.length - 1) {
      index += 1;
    } else {
      alert("The end of the lesson");
    }
  }

  function focusPrev() {
    if (index > 0) {
      index -= 1;
    } else {
      alert("The beginning of the lesson");
    }
  }
</script>

<main>
  {#each text.slice(0, index) as item}
    <ReadOnly targetText="{item.target}" typedText="{item.typed}" />
  {/each}
  <Typing switchNext={focusNext} switchPrevious={focusPrev} bind:targetText="{text[index].target}" bind:typedText="{text[index].typed}" />
  {#each text.slice(index+1) as item}
    <ReadOnly targetText="{item.target}" typedText="{item.typed}" />
  {/each}
</main>

<style>
</style>
