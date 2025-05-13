<script lang="ts">
  import ChapterSelect from './ChapterSelect.svelte';
  import Speedometer from "./Speedometer.svelte";

  export let selectedBook: string = '';
  export let selectedChapter: string = '';

  let isOpen = true;

  function togglePanel() {
    isOpen = !isOpen;
  }
</script>

<style>
  .side-panel {
    position: fixed;
    top: 0;
    right: 0;
    height: 100vh;
    background-color: #f4f4f4;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
    transition: width 0.3s ease;
    overflow: hidden;
    z-index: 1000;
  }

  .content {
    padding: 1rem;
  }

  .toggle-btn {
    position: fixed;
    top: 10px;
    right: 10px;
    width: 30px;
    height: 30px;
    border: none;
    border-radius: 0 4px 4px 0;
    cursor: pointer;
  }
</style>

<div class="side-panel" style="width: {isOpen ? '250px' : '0'}">
  <button class="toggle-btn" on:click={togglePanel}>
    {isOpen ? '→': '←' }
  </button>
  {#if isOpen}
    <div class="content">
      <ChapterSelect bind:selectedBook={selectedBook} bind:selectedChapter={selectedChapter} />
      <Speedometer />
    </div>
  {/if}
</div>
