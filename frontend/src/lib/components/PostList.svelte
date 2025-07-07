<script lang="ts">
	import { onMount } from 'svelte';

	type Post = {
		id: number;
		timestamp: number;
		title: string;
		slug: string;
		content: string;
	};

	let posts: Post[] = [];
	let loading = true;
	let error: string | null = null;

	onMount(async () => {
		try {
			const res = await fetch('http://127.0.0.1:8000/posts/');
			if (!res.ok) throw new Error(`Failed to fetch: ${res.status}`);

			posts = await res.json();
		} catch (e: any) {
			error = e.message;
		} finally {
			loading = false;
		}
	});
</script>

{#if loading}
	<p>Loading posts...</p>
{:else if error}
	<p style="color: red;">Error: {error}</p>
{:else}
	{#each posts as post}
		<article>
			<h1>{post.id}</h1>
			<h2>{post.title}</h2>
			<div>{@html post.content}</div>
		</article>
	{/each}
{/if}
