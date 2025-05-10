<script lang="ts">
  import Keyboard from "./Keyboard.svelte";

  let isOpen = false;

  function togglePanel() {
    isOpen = !isOpen;
  }
</script>

<style>
  .bottom-panel {
    position: fixed;
    bottom: 0;
    width: 60%;
    background-color: #f4f4f4;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
    transition: height 0.3s ease;
    overflow: hidden;
    z-index: 1000;
  }

  .content {
    padding: 1rem;
  }

  .toggle-btn {
    position: fixed;
    bottom: 10px;
    left: 10px;
    width: 30px;
    height: 30px;
    border: none;
    border-radius: 0 4px 4px 0;
    cursor: pointer;
  }
</style>

<div class="bottom-panel" style="height: {isOpen ? '220px' : '0'}">
  <button class="toggle-btn" on:click={togglePanel}>
    {isOpen ? '↓️': '⌨️' }
  </button>
  {#if isOpen}
    <div class="content">
      <Keyboard />
    </div>
  {/if}
</div>
