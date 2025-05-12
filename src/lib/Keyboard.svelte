<script lang="ts">
  import { onMount, onDestroy } from 'svelte';

  let {language = 'en_us'} = $props<{language: string}>();

  let pressedKeys = $state(new Set());

  const layouts = {
    'en_us': {
      'normal': [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'"],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
      ],
      'shift': [
        ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']
      ]
    },
    'ru_ru': {
      'normal': [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
        ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ'],
        ['ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', "э"],
        ['я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '/']
      ],
      'shift': [
        ['!', '"', '№', '%', ':', ',', '.', ';', '(', ')', '_', '+'],
        ['Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ'],
        ['Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', "Э"],
        ['Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', '?']
      ]
    }
  }
  let rows = $state(layouts[language]['normal']);
  const fingers = [
    ['lp', 'lr', 'lm', 'li', 'li', 'ri', 'ri', 'rm', 'rr', 'rp', 'rp', 'rp'],
    ['lp', 'lr', 'lm', 'li', 'li', 'ri', 'ri', 'rm', 'rr', 'rp', 'rp', 'rp'],
    ['lp hr', 'lr hr', 'lm hr', 'li hr', 'li', 'ri', 'ri hr', 'rm hr', 'rr hr', 'rp hr', 'rp'],
    ['lp', 'lr', 'lm', 'li', 'li', 'ri', 'ri', 'rm', 'rr', 'rp']
  ]

  const handleKeyDown = (e: KeyboardEvent) => {
    const key = e.key; // .toUpperCase();
    pressedKeys.add(key);
    pressedKeys = new Set(pressedKeys); // Hack to re-draw on change
    if (e.shiftKey) {
      rows = layouts[language]['shift'];
    }
  };

  const handleKeyUp = (e: KeyboardEvent) => {
    setTimeout(() => { // Hack to show the pressed key for a bit longer
      const key = e.key; // .toUpperCase();
      pressedKeys.delete(key);
      pressedKeys = new Set(pressedKeys);
    }, 300)
    if (!e.shiftKey) {
      rows = layouts[language]['normal'];
    }
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
    transform: scale(1.2);
  }
  .key.hr {
    border: 1px solid black;
  }
  .key.lp {
    background: lightblue;
  }
  .key.lr {
    background: lightgreen;
  }
  .key.lm {
    background: lightyellow;
  }
  .key.li {
    background: lightsteelblue;
  }
  .key.ri {
    background: lightcoral;
  }
  .key.rm {
    background: lightpink;
  }
  .key.rr {
    background: lightseagreen;
  }
  .key.rp {
    background: lightcyan
  }
</style>

<div class="keyboard">
  {#each rows as row, i}
    <div class="row">
      {#each row as key, y}
        <div class="key {pressedKeys.has(key) ? 'active' : fingers[i][y]} ">
          {key}
        </div>
      {/each}
    </div>
  {/each}
</div>
