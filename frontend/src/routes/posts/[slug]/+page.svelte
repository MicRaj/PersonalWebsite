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
			const res = await fetch(`/api/posts/slug/${slug}`);
			if (!res.ok) throw new Error(`Failed to fetch: ${res.status}`);
			post = await res.json();
		} catch (e: any) {
			error = e.message;
		}
	});
</script>

<div class="container">
	{#if post}
		<h1>{post.title}</h1>
		<!-- <img src={post.cover_image} alt={post.title} /> -->
		<p>{@html post.content}</p>
	{:else if error}
		<p>{error}</p>
	{:else}
		<p>Loading...</p>
	{/if}
</div>

<style>
	/* Center everything vertically and horizontally */
	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		min-height: 100vh; /* full viewport height */
		padding: 1rem;
		box-sizing: border-box;
		background-color: #f9f9f9;
	}

	h1 {
		font-size: 2rem;
		margin-bottom: 1rem;
		text-align: center;
	}

	img {
		max-width: 100%;
		height: auto;
		margin-bottom: 1rem;
		border-radius: 8px;
		box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
	}

	p {
		max-width: 600px;
		line-height: 1.6;
		text-align: justify;
		font-size: 1rem;
		color: #333;
	}
</style>
