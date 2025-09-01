<script lang="ts">
	import { page } from '$app/state';
	import { onMount } from 'svelte';
	type Post = {
		id: number;
		timestamp: number;
		title: string;
		slug: string;
		content: string;
		cover_image: string;
	};

	let post: Post | null = null;
	let error: string | null = null;

	onMount(async () => {
		const slug = page.params.slug; // get the slug from URL
		try {
			const res = await fetch(`/api/posts/${slug}`);
			if (!res.ok) throw new Error(`Failed to fetch: ${res.status}`);
			post = await res.json();
		} catch (e: any) {
			error = e.message;
		}
	});
</script>

{#if post}
	<h1>{post.title}</h1>
	<img src={post.cover_image} alt={post.title} />
	<p>{post.content}</p>
{:else if error}
	<p>{error}</p>
{:else}
	<p>Loading...</p>
{/if}
