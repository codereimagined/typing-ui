<script lang="ts">
  import Typing from './lib/Typing.svelte'
  import ReadOnly from './lib/ReadOnly.svelte'
  import ChapterSelect from "./lib/ChapterSelect.svelte";

  let textObjects = [ // Default text if loading failed
    { target: "The quick brown fox jumped over the lazy dog ", typed: "" },
    { target: "End of the story!", typed: "" }
  ];
  let index = 0;

  let chapters = [
    {label: "Chapter 1", value: "oliver-twist-chapter-1.txt"},
    {label: "Chapter 2", value: "oliver-twist-chapter-2.txt"},
    {label: "Chapter 3", value: "oliver-twist-chapter-3.txt"},
    {label: "Chapter 4", value: "oliver-twist-chapter-4.txt"},
    {label: "Chapter 5", value: "oliver-twist-chapter-5.txt"}
  ]
  let selectedChapter = chapters[0].value;

  $: fetch(selectedChapter)
    .then(response => response.text())
    .then(text => {
      textObjects = text.split('\n').map(line => {
        return { target: line + " ", typed: "" }
      });
      index = 0;
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
  <ChapterSelect bind:selectedChapter={selectedChapter} options={chapters}/>
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
