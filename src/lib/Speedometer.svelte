<script lang="ts">
  import { message, pastMessages } from './sharedStore';
</script>

<div>
  <p>{$message}</p>
  {#if $pastMessages.length > 0}<p>--- Previous results ---</p>{/if}
  {#each $pastMessages as item}
    <p>{item}</p>
  {/each}
</div>

<style>
</style>
