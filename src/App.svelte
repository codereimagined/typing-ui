<script lang="ts">
  import Typing from './lib/Typing.svelte'
  import ReadOnly from './lib/ReadOnly.svelte'
  import SidePanel from "./lib/SidePanel.svelte";
  import BottomPanel from "./lib/BottomPanel.svelte";

  let textObjects = [ // Default text if loading failed
    { target: "The quick brown fox jumped over the lazy dog ", typed: "", fixIndexes: new Set<number>() },
    { target: "End of the story!", typed: "", fixIndexes: new Set<number>() }
  ];
  let index = 0;

  let selectedBook = localStorage.getItem("selectedBook") ?? "oliver-twist";
  let selectedChapter = localStorage.getItem(`${selectedBook}-selectedChapter`) ?? "chapter-1.txt";
  type BookInfo = {
      [key: string]: { language: string }
  }

  let booksInfo: BookInfo = {
      'oliver-twist': {language: 'en_us'},
      'anna-karenina-part-1': {language: 'ru_ru'},
    }
  $: fetch(`${selectedBook}/${selectedChapter}`)
    .then(response => response.text())
    .then(text => {
      textObjects = text.split('\n').map(line => {
        return { target: line + " ", typed: "", fixIndexes: new Set<number>() }
      });
      localStorage.setItem(`${selectedBook}-selectedChapter`, selectedChapter);
      index = parseInt(localStorage.getItem(`${selectedBook}-${selectedChapter}`) || "0", 10);
    })
    .catch(error => {
      alert("Error fetching text");
      console.error('Error fetching text:', error);
    });

  function focusNext() {
    if (index < textObjects.length - 1) {
      index += 1;
      localStorage.setItem(`${selectedBook}-${selectedChapter}`, index.toString());
    } else {
      alert("The end of the lesson");
    }
  }

  function focusPrev() {
    if (index > 0) {
      index -= 1;
      localStorage.setItem(`${selectedBook}-${selectedChapter}`, index.toString());
    } else {
      alert("The beginning of the lesson");
    }
  }
</script>

<main>
  <SidePanel bind:selectedBook={selectedBook} bind:selectedChapter={selectedChapter} />
  <BottomPanel language={booksInfo[selectedBook].language}/>
  {#each textObjects.slice(0, index) as item}
    <ReadOnly targetText="{item.target}" typedText="{item.typed}" fixIndexes="{item.fixIndexes}"/>
  {/each}
  <Typing switchNext={focusNext}
          switchPrevious={focusPrev}
          targetText="{textObjects[index].target}"
          bind:typedText="{textObjects[index].typed}"
          bind:fixIndexes="{textObjects[index].fixIndexes}" />
  {#each textObjects.slice(index+1) as item}
    <ReadOnly targetText="{item.target}" />
  {/each}
  <div class="spacer" style="height: 12rem"></div>
</main>

<style>
</style>
