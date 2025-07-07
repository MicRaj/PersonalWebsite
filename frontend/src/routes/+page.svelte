<script lang="ts">
	import PostList from '$lib/components/PostList.svelte';
	import TinyEditor from '$lib/components/TinyEditor.svelte';
	let content: string = '<p>Hello, TinyMCE!</p>';
</script>

<h1>My Editor</h1>
<TinyEditor bind:content height={400} />
<PostList />

<!-- <h2>Preview:</h2>
<div>{@html content}</div> -->
