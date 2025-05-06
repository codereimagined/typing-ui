<script lang="ts">
  export let chapters: { label: string; value: string }[] = [];
  export let selectedChapter: string = '';
</script>

<div class="chapter-select" id="chapter-select">
  <select bind:value={selectedChapter}>
    <option disabled selected={selectedChapter === ''} value="">
      Jump to a chapter...
    </option>
    {#each chapters as item}
      <option value={item.value}>{item.label}</option>
    {/each}
  </select>
</div>

<style>
</style>
