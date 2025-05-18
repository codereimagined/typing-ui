<script lang="ts">
  export let selectedBook: string = '';
  export let selectedChapter: string = '';

  interface Chapter {
    label: string;
    value: string;
  }

  interface Book {
    label: string;
    value: string;
    chapters: Chapter[];
  }

  let books: Record<string, Book> = {
    'oliver-twist': {label: 'Oliver Twist', value: 'oliver-twist', chapters: []},
    'anna-karenina-part-1': {label: 'Анна Каренина', value: 'anna-karenina-part-1', chapters: []}
  }
  // let chapters = [];
  for (let i = 1; i <= 53; i++) { // Here 53 is a number of chapters
    books['oliver-twist'].chapters.push({label: `Chapter ${i}`, value: `chapter-${i}.txt`});
  }
  for (let i = 1; i <= 33; i++) { // Here 53 is a number of chapters
    books['anna-karenina-part-1'].chapters.push({label: `Chapter ${i}`, value: `chapter-${i}.txt`});
  }

</script>

<div class="chapter-select" id="chapter-select">
  <h2>{books[selectedBook].label}</h2>
  <select bind:value={selectedBook}>
    <option disabled selected={selectedBook === ''} value="">
      Jump to a book...
    </option>
    {#each Object.values(books) as item}
      <option value={item.value}>{item.label}</option>
    {/each}
  </select>
  <select bind:value={selectedChapter}>
    <option disabled selected={selectedChapter === ''} value="">
      Jump to a chapter...
    </option>
    {#each books[selectedBook].chapters as item}
      <option value={item.value}>{item.label}</option>
    {/each}
  </select>
</div>

<style>
</style>
