<script>
	import { onMount } from 'svelte';

	const sections = ['welcome', 'projects', 'about'];

	onMount(() => {
		const navLinks = document.querySelectorAll('.sidebar nav ul li a');

		navLinks.forEach((link) => {
			link.addEventListener('click', (event) => {
				event.preventDefault();

				const targetId = link.getAttribute('href').substring(1);
				const targetSection = document.getElementById(targetId);

				if (targetSection) {
					targetSection.scrollIntoView({ behavior: 'smooth' });
				}
			});
		});
	});
</script>

<div class="app">
	<!-- Sidebar -->
	<aside class="sidebar">
		<nav>
			<ul>
				{#each sections as section}
					<li>
						<a href={`#${section}`}>{section.charAt(0).toUpperCase() + section.slice(1)}</a>
					</li>
				{/each}
			</ul>
		</nav>
		<!-- <div class="social-icons">
			<a href="#"
				><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" /></a
			>
			<a href="#"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" /></a>
		</div> -->
	</aside>

	<!-- Main content -->
	<main class="content">
		<section id="welcome">
			<h1>Hi! I’m Michal,<br />welcome to<br />my blog</h1>
		</section>

		<section id="projects">
			<div class="project-card red">
				<img src="https://via.placeholder.com/100x80?text=Macro" alt="Macropad" />
				<div class="text">
					<h3>Macropad</h3>
					<p class="date">08/07/2025</p>
					<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
				</div>
			</div>

			<div class="project-card purple">
				<img src="https://via.placeholder.com/100x80?text=Cloud" alt="Self-hosted website" />
				<div class="text">
					<h3>Self-hosted website</h3>
					<p class="date">08/07/2025</p>
					<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
				</div>
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

	.sidebar {
		width: 150px;
		background-color: #f1f9c6;
		border-right: 2px solid #d3e4a3;
		padding: 20px 10px;
		position: sticky;
		top: 0;
		height: 100vh;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}

	.content {
		flex: 1;
		overflow-y: scroll;
		scroll-snap-type: y mandatory;
		scroll-behavior: smooth;
	}

	section {
		min-height: 100vh;
		padding: 40px;
		background-color: #f1f9c6;
		scroll-snap-align: start;
	}

	/* Sidebar */
	ul {
		list-style: none;
		padding: 0;
		line-height: 2.5;
	}

	li a {
		text-decoration: none;
		color: #222;
		font-weight: 500;
	}

	li a:hover {
		color: #006699;
	}

	.social-icons img {
		width: 24px;
		margin: 10px 0;
		cursor: pointer;
	}

	/* Welcome Section */
	#welcome h1 {
		font-size: 2.5rem;
		color: #214c4e;
		line-height: 1.5;
	}

	/* Projects Section */
	#projects {
		display: flex;
		flex-direction: column;
		gap: 20px;
	}

	.project-card {
		display: flex;
		color: white;
		padding: 20px;
		border-radius: 10px;
		box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
		align-items: center;
		gap: 20px;
	}

	.red {
		background-color: #e74c3c;
	}

	.purple {
		background-color: #dd5edb;
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
	#about h2 {
		color: #214c4e;
		font-size: 2rem;
		margin-bottom: 10px;
	}

	#about p {
		font-size: 1.1rem;
		max-width: 600px;
	}
</style>
