<script lang="ts">
  export let options: { label: string; value: string }[] = [];
  export let selectedChapter: string = '';
</script>

<div class="chapter-select" id="chapter-select">
  <select bind:value={selectedChapter}>
    <option disabled selected={selectedChapter === ''} value="">
      Jump to a chapter...
    </option>
    {#each options as option}
      <option value={option.value}>{option.label}</option>
    {/each}
  </select>
</div>

<style>
</style>
