<script>
	import { onMount } from 'svelte';
	import SideBar from '$lib/components/SideBar.svelte';

	const sections = ['welcome', 'projects', 'about'];
	const blogs = [
		{
			title: 'Macropad',
			date: '08/07/2025',
			excerpt: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
			image: 'https://via.placeholder.com/100x80?text=Macro'
		},
		{
			title: 'Self-hosted website',
			date: '08/07/2025',
			excerpt: 'Learn how I hosted my personal website using open-source tools.',
			image: 'https://via.placeholder.com/100x80?text=Cloud'
		},
		{
			title: 'Macropad',
			date: '08/07/2025',
			excerpt: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
			image: 'https://via.placeholder.com/100x80?text=Macro'
		},
		{
			title: 'Self-hosted website',
			date: '08/07/2025',
			excerpt: 'Learn how I hosted my personal website using open-source tools.',
			image: 'https://via.placeholder.com/100x80?text=Cloud'
		},
		{
			title: 'Macropad',
			date: '08/07/2025',
			excerpt: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
			image: 'https://via.placeholder.com/100x80?text=Macro'
		},
		{
			title: 'Self-hosted website',
			date: '08/07/2025',
			excerpt: 'Learn how I hosted my personal website using open-source tools.',
			image: 'https://via.placeholder.com/100x80?text=Cloud'
		},
		{
			title: 'Macropad',
			date: '08/07/2025',
			excerpt: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
			image: 'https://via.placeholder.com/100x80?text=Macro'
		},
		{
			title: 'Self-hosted website',
			date: '08/07/2025',
			excerpt: 'Learn how I hosted my personal website using open-source tools.',
			image: 'https://via.placeholder.com/100x80?text=Cloud'
		},
		{
			title: 'Self-hosted website',
			date: '08/07/2025',
			excerpt: 'Learn how I hosted my personal website using open-source tools.',
			image: 'https://via.placeholder.com/100x80?text=Cloud'
		},
		{
			title: 'Self-hosted website',
			date: '08/07/2025',
			excerpt: 'Learn how I hosted my personal website using open-source tools.',
			image: 'https://via.placeholder.com/100x80?text=Cloud'
		},
		{
			title: 'Self-hosted website',
			date: '08/07/2025',
			excerpt: 'Learn how I hosted my personal website using open-source tools.',
			image: 'https://via.placeholder.com/100x80?text=Cloud'
		},
		{
			title: 'Self-hosted website',
			date: '08/07/2025',
			excerpt: 'Learn how I hosted my personal website using open-source tools.',
			image: 'https://via.placeholder.com/100x80?text=Cloud'
		},
		{
			title: 'Self-hosted website',
			date: '08/07/2025',
			excerpt: 'Learn how I hosted my personal website using open-source tools.',
			image: 'https://via.placeholder.com/100x80?text=Cloud'
		},
		{
			title: 'Self-hosted website',
			date: '08/07/2025',
			excerpt: 'Learn how I hosted my personal website using open-source tools.',
			image: 'https://via.placeholder.com/100x80?text=Cloud'
		},
		{
			title: 'Self-hosted website',
			date: '08/07/2025',
			excerpt: 'Learn how I hosted my personal website using open-source tools.',
			image: 'https://via.placeholder.com/100x80?text=Cloud'
		},
		{
			title: 'Self-hosted website',
			date: '08/07/2025',
			excerpt: 'Learn how I hosted my personal website using open-source tools.',
			image: 'https://via.placeholder.com/100x80?text=Cloud'
		}
	];
</script>

<div class="app">
	<SideBar {sections} />

	<!-- Main content -->
	<main class="content">
		<section id="welcome">
			<h1>Hi! I'm Michal,<br />Welcome to<br />my blog</h1>
		</section>

		<section id="projects">
			<div class="sticky-header">
				<h2>Projects</h2>
				<hr class="projects-line" />
			</div>
			<div class="blog-grid">
				{#each blogs as blog}
					<div class="blog-card">
						<img src="hamster_angry.jpg" alt={blog.title} />
						<div class="content">
							<h3>{blog.title}</h3>
							<p class="date">{blog.date}</p>
							<p class="excerpt">{blog.excerpt}</p>
						</div>
					</div>
				{/each}
			</div>
		</section>

		<section id="about">
			<h2>About Me</h2>
			<p>This is a short bio about Michal. You can customize this section however you like.</p>
		</section>
	</main>
</div>

<style>
	/* Layout */
	.app {
		display: flex;
		height: 100vh;
		overflow: hidden;
		font-family: 'Segoe UI', sans-serif;
	}

	.content {
		flex: 1;
		overflow-y: scroll;
		scroll-snap-type: y mandatory;
		scroll-behavior: smooth;
	}

	section {
		min-height: 90vh;
		height: auto;
		padding: 40px;
		scroll-snap-align: start;
		/* scroll-padding-top: 60px; */
	}

	/* Welcome Section */
	#welcome {
		display: flex;
		justify-content: center; /* Center horizontally */
		align-items: center; /* Center vertically */
		text-align: left;
		min-height: 95vh; /* already present */
		padding: 40px;
	}

	#welcome h1 {
		font-size: clamp(3.2rem, 8vw, 5.5em);
		color: #1c5253;
		line-height: 1.5;
		font-family: 'Space Grotesk', sans-serif;
		margin: 0;
		padding-bottom: 100px;
	}

	#projects {
		padding: 0 10px; /* horizontal padding instead of fixed width */
		display: flex;
		flex-direction: column;
		gap: 20px;
		position: relative;
		max-width: 1200px; /* optional max width */
		margin: 0 auto; /* center it */
	}

	/* Sticky header */
	.sticky-header {
		position: sticky;
		top: 0;
		background-color: #f3ffc6;
		z-index: 10;
		display: flex;
		flex-direction: column;
		padding-left: 40px; /* match the #projects padding */
		padding-right: 40px;
	}

	#projects h2 {
		background-color: #f3ffc6;
		padding-left: 0;
		padding-right: 0;
		margin: 20px 0 0 0;
		z-index: 11;
		color: #214c4e;
		font-size: 2rem;
	}

	.projects-line {
		width: calc(100% -2px);
		height: 4px;
		background-color: #1c5253;
		margin: 0;
		margin-top: 8px;
		position: sticky;
		top: 44px; /* height of the h2 + some space */
		z-index: 10;
	}
	/* 3-column grid */
	.blog-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
		gap: 24px;
		padding: 20px 40px 100px; /* top 20, left/right 40 (match section) */
	}

	.blog-card {
		background: white;
		border: 2px solid #1c5253;
		border-radius: 10px;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
		overflow: hidden;
		transition:
			transform 0.2s ease,
			box-shadow 0.2s ease;
		display: flex;
		flex-direction: column;
	}

	.blog-card:hover {
		transform: translateY(-4px);
		box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
	}

	.blog-card img {
		width: 100%;
		height: 180px;
		object-fit: cover;
	}

	.blog-card .content {
		padding: 20px;
	}

	.blog-card h3 {
		margin: 0 0 8px;
		color: #333;
		font-size: 1.3rem;
	}

	.blog-card .date {
		color: #888;
		font-size: 0.9rem;
		margin-bottom: 12px;
	}

	.blog-card .excerpt {
		color: #555;
		font-size: 1rem;
	}

	.project-card {
		display: flex;
		color: white;
		padding: 20px;
		border-radius: 10px;
		box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
		align-items: center;
		gap: 20px;
		height: 40vh;
	}

	.red {
		background-color: #e74c3c;
	}

	.purple {
		background-color: #dd5edb;
	}

	#projects h2 {
		color: #214c4e;
		font-size: 2rem;
		margin-bottom: 20px;
	}
	.project-card img {
		width: 100px;
		border-radius: 5px;
	}

	.date {
		font-size: 0.9em;
		opacity: 0.9;
		margin-bottom: 10px;
	}

	/* About Section */
	#about {
		padding-top: 0px;
	}
	#about h2 {
		color: #214c4e;
		font-size: 2rem;
		margin-bottom: 10px;
	}

	#about p {
		font-size: 1.1rem;
		max-width: 600px;
	}

	:global(body) {
		background-color: #f3ffc6;
		margin: 0;
		font-family: 'Space Grotesk', sans-serif;
	}
</style>
