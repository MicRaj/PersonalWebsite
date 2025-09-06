<script lang="ts">
	import { onMount } from 'svelte';

	type Post = {
		id: number;
		timestamp: number;
		title: string;
		slug: string;
		content: string;
		cover_image: string;
	};

	let posts: Post[] = [];
	let loading = true;
	let error: string | null = null;

	onMount(async () => {
		try {
			const res = await fetch('/api/posts/');
			if (!res.ok) throw new Error(`Failed to fetch: ${res.status}`);
			posts = await res.json();
		} catch (e: any) {
			error = e.message;
		} finally {
			loading = false;
		}
	});
</script>

<!-- Post Grid -->
<div class="post-grid">
	{#each posts as post}
		<a class="post-card" href={`/posts/${post.slug}`}>
			<img src={post.cover_image} alt={post.title} />
			<div class="content">
				<h3>{post.title}</h3>
				<p class="date">{new Date(post.timestamp).toLocaleDateString()}</p>
				<!-- <p class="excerpt">{post.content}</p> -->
			</div>
		</a>
	{/each}
</div>

<style>
	.post-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
		gap: 24px;
		padding: 20px 40px;
	}
	.post-card {
		background: var(--color-white);
		border: 2px solid var(--color-primary);
		border-radius: 10px;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
		transition:
			transform 0.2s ease,
			box-shadow 0.2s ease;
		display: flex;
		flex-direction: column;
		overflow: hidden;
	}
	a.post-card {
		text-decoration: none;
		color: inherit;
	}
	.post-card:hover {
		transform: translateY(-4px);
		box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
	}
	.post-card img {
		width: 100%;
		height: 180px;
		object-fit: cover;
	}
	.post-card .content {
		padding: 20px;
	}
	.post-card h3 {
		margin: 0 0 8px;
		color: var(--color-heading);
		font-size: 1.3rem;
	}
	.post-card .date {
		color: var(--color-muted);
		font-size: 0.9rem;
		margin-bottom: 12px;
	}
	.post-card .excerpt {
		color: var(--color-subtext);
		font-size: 1rem;
	}
	.date {
		font-size: 0.9em;
		opacity: 0.9;
		margin-bottom: 10px;
	}
</style>
