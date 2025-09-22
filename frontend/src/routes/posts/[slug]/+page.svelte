<script lang="ts">
	import { page } from '$app/state';
	import { onMount } from 'svelte';
	import SideBarPost from '$lib/components/SideBarPost.svelte';
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

<div class="app">
	<SideBarPost />
	<main class="content">
		<div class="post-container">
			{#if post}
				<div class="heading-image" style="background-image: url('{post.cover_image}')"></div>
				<div class="post-tile">
					<h1>{post.title}</h1>
					<div class="post-content">
						<p>{@html post.content}</p>
					</div>
				</div>
			{:else if error}
				<p>{error}</p>
			{:else}
				<p>Loading...</p>
			{/if}
		</div>
	</main>
</div>

<style>
	:global(html, body) {
		height: 100%;
		margin: 0;
		padding: 0;
	}

	.app {
		display: flex;
		height: 100vh;
		overflow: hidden;
		font-family: var(--font-body);
		background: var(--color-background);
	}
	.content {
		flex: 1;
		overflow-y: scroll;
		padding: 0;
		margin: 0;
		/* scroll-snap-type: y mandatory;
		scroll-behavior: smooth; */

		/* Hide scrollbar */
		/* scrollbar-width: none;
		-ms-overflow-style: none;
		user-select: none; */
	}

	.post-container {
		flex: 1;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		min-height: 100vh;
		max-width: 900px;
		width: 90%;
		margin: 0 auto;
		padding: 0;
		user-select: text;
		border-left: 1px solid rgba(0, 0, 0, 0.05);
		border-right: 1px solid rgba(0, 0, 0, 0.05);
	}
	.post-container .post-tile {
		padding: 0 1.2rem 0 1.2rem;
	}
	.post-container h1 {
		font-size: clamp(2rem, 6vw, 3rem);
		font-weight: 800;
		margin-top: 0;
		margin-bottom: 1.5rem;
		text-align: center;
		color: var(--color-primary-text);
		line-height: 1.2;
		position: relative;
	}

	/* Add a subtle underline accent */
	.post-container h1::after {
		content: '';
		display: block;
		width: 60px;
		height: 4px;
		margin: 0.5rem auto 0;
		background: linear-gradient(90deg, #03045e, #8d5a97);
		border-radius: 2px;
	}
	.heading-image {
		background-image: url('cover.jpg');
		background-size: cover;
		background-position: center;
		width: 100%;
		height: 120px;
	}

	/* Mobile adjustments */
	@media (max-width: 768px) {
		.post-container {
			width: 100%;
			margin: 0;
		}
		.heading-image {
			height: 50px;
		}

		/* sidebar is hidden via its own CSS already */
	}
</style>
