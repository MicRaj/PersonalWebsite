import adapter from '@sveltejs/adapter-node';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

export default {
  kit: {
    preprocess: vitePreprocess(),
    adapter: adapter({
      out: 'build'  // output folder for the Node server build
    })
  }
};
