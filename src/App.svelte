<script lang="ts">
  import Typing from './lib/Typing.svelte'
  import ReadOnly from './lib/ReadOnly.svelte'

  let textObjects = [ // Default text if loading failed
    { target: "a quick brown fox jumped over the lazy dog ", typed: "" },
    { target: "type something from outside... ", typed: "" },
    { target: "more typing of cool text ", typed: "" },
    { target: "the story of Oliver continues... ", typed: ""},
    { target: "end of the story!", typed: "" }
  ];
  let index = 0;

  fetch('oliver-twist-chapter-i.txt')
    .then(response => response.text())
    .then(text => {
      textObjects = text.split('\n').map(line => {
        return { target: line + " ", typed: "" }
      })
    })
    .catch(error => {
      alert("Error fetching text");
      console.error('Error fetching text:', error);
    });

  function focusNext() {
    if (index < textObjects.length - 1) {
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
  {#each textObjects.slice(0, index) as item}
    <ReadOnly targetText="{item.target}" typedText="{item.typed}" />
  {/each}
  <Typing switchNext={focusNext} switchPrevious={focusPrev} bind:targetText="{textObjects[index].target}" bind:typedText="{textObjects[index].typed}" />
  {#each textObjects.slice(index+1) as item}
    <ReadOnly targetText="{item.target}" typedText="{item.typed}" />
  {/each}
</main>

<style>
</style>
