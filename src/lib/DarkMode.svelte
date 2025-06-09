<script lang="ts">
  import { onMount } from 'svelte';

  let darkMode = false;

  // Save preference in localStorage
  function toggleDarkMode() {
    darkMode = !darkMode;
    document.documentElement.classList.toggle('dark', darkMode);
    localStorage.setItem('darkMode', darkMode.toString());
  }

  onMount(() => {
    // Load saved preference
    darkMode = localStorage.getItem('darkMode') === 'true';
    document.documentElement.classList.toggle('dark', darkMode);
  });
</script>

<button on:click={toggleDarkMode}>
  {darkMode ? '🌙 Dark Mode On' : '☀️ Light Mode'}
</button>
