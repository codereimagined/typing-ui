<script lang="ts">
  import { onMount, onDestroy } from 'svelte';

  let pressedKeys = $state(new Set());

  const rows = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.']
  ];

  const handleKeyDown = (e: KeyboardEvent) => {
    const key = e.key.toUpperCase();
    pressedKeys.add(key);
    pressedKeys = new Set(pressedKeys); // Hack to re-draw on change
  };

  const handleKeyUp = (e: KeyboardEvent) => {
    setTimeout(() => { // Hack to show the pressed key for a bit longer
      const key = e.key.toUpperCase();
      pressedKeys.delete(key);
      pressedKeys = new Set(pressedKeys);
    }, 300)
  };

  onMount(() => {
    window.addEventListener('keydown', handleKeyDown);
    window.addEventListener('keyup', handleKeyUp);
  });

  onDestroy(() => {
    window.removeEventListener('keydown', handleKeyDown);
    window.removeEventListener('keyup', handleKeyUp);
  });
</script>

<style>
  .keyboard {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    align-items: center;
    font-family: sans-serif;
  }

  .row {
    display: flex;
    gap: 0.5rem;
  }

  .key {
    width: 40px;
    height: 40px;
    background: #eee;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-align: center;
    line-height: 40px;
    font-weight: bold;
    transition: background 0.2s, transform 0.1s;
  }

  .key.active {
    background: #4caf50;
    color: white;
    transform: scale(1.1);
  }
</style>

<div class="keyboard">
  {#each rows as row}
    <div class="row">
      {#each row as key}
        <div class="key {pressedKeys.has(key) ? 'active' : ''}">
          {key}
        </div>
      {/each}
    </div>
  {/each}
</div>
