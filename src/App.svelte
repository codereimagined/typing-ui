<script lang="ts">
  import Typing from './lib/Typing.svelte'
  import ReadOnly from './lib/ReadOnly.svelte'
  import SidePanel from "./lib/SidePanel.svelte";

  let textObjects = [ // Default text if loading failed
    { target: "The quick brown fox jumped over the lazy dog ", typed: "" },
    { target: "End of the story!", typed: "" }
  ];
  let index = 0;

  let chapters = [];
  for (let i = 1; i <= 53; i++) { // Here 53 is a number of chapters
      chapters.push({label: `Chapter ${i}`, value: `oliver-twist/chapter-${i}.txt`});
  }
  let selectedChapter = localStorage.getItem("selectedChapter") ?? "oliver-twist/chapter-1.txt";

  $: fetch(selectedChapter)
    .then(response => response.text())
    .then(text => {
      textObjects = text.split('\n').map(line => {
        return { target: line + " ", typed: "" }
      });
      localStorage.setItem("selectedChapter", selectedChapter);
      index = parseInt(localStorage.getItem(selectedChapter) || "0", 10);
    })
    .catch(error => {
      alert("Error fetching text");
      console.error('Error fetching text:', error);
    });

  function focusNext() {
    if (index < textObjects.length - 1) {
      index += 1;
      localStorage.setItem(selectedChapter, index.toString());
    } else {
      alert("The end of the lesson");
    }
  }

  function focusPrev() {
    if (index > 0) {
      index -= 1;
      localStorage.setItem(selectedChapter, index.toString());
    } else {
      alert("The beginning of the lesson");
    }
  }
</script>

<main>
  <SidePanel bind:selectedChapter={selectedChapter} chapters={chapters} />
  {#each textObjects.slice(0, index) as item}
    <ReadOnly targetText="{item.target}" typedText="{item.typed}" />
  {/each}
  <Typing switchNext={focusNext} switchPrevious={focusPrev} targetText="{textObjects[index].target}" bind:typedText="{textObjects[index].typed}" />
  {#each textObjects.slice(index+1) as item}
    <ReadOnly targetText="{item.target}" typedText="{item.typed}" />
  {/each}
  <div class="spacer" style="height: 12rem"></div>
</main>

<style>
</style>
