import { writable } from 'svelte/store';

export const message  = writable('');
export const pastMessages = writable([]);
