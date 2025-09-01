<script>
	import { onMount, tick } from 'svelte';
	import SideBar from '$lib/components/SideBar.svelte';
	import PostGrid from '$lib/components/PostGrid.svelte';
	import { fade } from 'svelte/transition';
	import { cubicOut } from 'svelte/easing';

	const sections = ['welcome', 'projects', 'about'];
	let show = false;

	onMount(() => {
		const observerTarget = document.querySelector('#welcome');
		if (!observerTarget) return;

		const observer = new IntersectionObserver(
			async (entries) => {
				for (const entry of entries) {
					if (entry.isIntersecting) {
						// Unmount to reset fade
						show = false;
						await tick(); // wait for DOM update

						// Mount to trigger fade-in
						show = true;

						await tick();

						// Restart wave animation
						const waveEl = document.querySelector('.hand');
						if (waveEl) {
							waveEl.classList.remove('wave');
							void waveEl.offsetWidth; // trigger reflow
							waveEl.classList.add('wave');
						}
					} else {
						show = false; // unmount when out of view
					}
				}
			},
			{ threshold: 0.2 }
		);

		observer.observe(observerTarget);

		return () => observer.disconnect();
	});
</script>

<div class="app">
	<SideBar {sections} />

	<main class="content">
		<!-- Welcome -->
		<section id="welcome" class="section welcome-section">
			{#if show}
				<h1 in:fade={{ duration: 1000, delay: 100, easing: cubicOut }}>
					Hi! I'm Michal,<br />Welcome to<br />my blog
					<span class="hand" aria-label="waving hand" role="img">
						<span class="wave">👋</span>
					</span>
				</h1>

				<!-- Up and Down Arrow SVG -->
				<div class="scroll-indicator" in:fade={{ duration: 2000, delay: 3000, easing: cubicOut }}>
					<img src="/icons/double-arrow-down.svg" alt="arrow" />
				</div>
			{/if}
		</section>

		<!-- Projects -->
		<section id="projects" class="section projects-section">
			<div class="section-header">
				<h2>Projects</h2>
				<hr />
			</div>

			<!-- Blog Grid -->
			<PostGrid />

			<div id="projects-exit-anchor" class="exit-anchor snap-scroll-bottom"></div>
		</section>

		<!-- About -->
		<section id="about" class="section about-section">
			<div class="section-header">
				<h2>About me</h2>
				<hr />
			</div>

			<div class="about-content">
				<p>This is a short bio about Michal. You can customize this section however you like.</p>
			</div>

			<div id="about-exit-anchor" class="exit-anchor"></div>
		</section>
	</main>
</div>

<style>
	:root {
		--color-bg: #ebebeb;
		--color-primary: #1c5253;
		--color-secondary: #214c4e;
		--color-heading: #333;
		--color-subtext: #555;
		--color-muted: #888;
		--color-white: #ffffff;

		--font-body: 'Segoe UI', sans-serif;
		--font-heading: 'Space Grotesk', sans-serif;
	}

	:global(body) {
		background-color: var(--color-bg);
		margin: 0;
		font-family: var(--font-heading);
	}

	.app {
		display: flex;
		height: 100vh;
		overflow: hidden;
		font-family: var(--font-body);
	}

	.content {
		flex: 1;
		overflow-y: scroll;
		scroll-snap-type: y mandatory;
		scroll-behavior: smooth;

		/* Hide scrollbar */
		scrollbar-width: none;
		-ms-overflow-style: none;
		user-select: none;
	}

	/* Hide scrollbar for WebKit browsers */
	.content::-webkit-scrollbar {
		display: none;
	}

	.section {
		min-height: 100vh;
		max-width: 1600px;
		padding: 40px;
		scroll-snap-align: start;
		scroll-snap-stop: always;
		margin: 0 auto;
		display: flex;
		flex-direction: column;
		gap: 20px;
	}

	/* Welcome */
	.welcome-section {
		justify-content: center;
		align-items: center;
		min-height: 95vh;
	}
	.welcome-fade-content {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		width: 100%;
		height: 100%;
		text-align: center;
	}
	.welcome-section h1 {
		font-size: clamp(3.2rem, 8vw, 8em);
		color: var(--color-primary);
		line-height: 1.5;
		font-family: var(--font-heading);
		margin: 0;
		padding-bottom: 100px;
		text-align: left;
	}
	.scroll-indicator {
		top: 200px;
		transform: translateX(-50%);
	}

	.scroll-indicator img {
		width: clamp(50px, 8vw, 100px);
		height: auto;
		animation: arrowUpDown 1.5s infinite;
	}

	@keyframes arrowUpDown {
		0%,
		100% {
			transform: translateY(0);
		}
		50% {
			transform: translateY(8px);
		}
	}

	/* Projects */
	.blog-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
		gap: 24px;
		padding: 20px 40px;
	}

	.blog-card {
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
		color: var(--color-heading);
		font-size: 1.3rem;
	}
	.blog-card .date {
		color: var(--color-muted);
		font-size: 0.9rem;
		margin-bottom: 12px;
	}
	.blog-card .excerpt {
		color: var(--color-subtext);
		font-size: 1rem;
	}
	.date {
		font-size: 0.9em;
		opacity: 0.9;
		margin-bottom: 10px;
	}

	/* About */
	.about-content {
		padding: 20px 40px 100px;
	}

	/* Utilities */
	.section-header {
		background-color: var(--color-bg);
		position: relative;
		top: 0;
		z-index: 10;
		display: flex;
		flex-direction: column;
		padding: 0 40px;
	}

	.section-header h2 {
		margin: 0;
		color: var(--color-secondary);
		font-size: 2rem;
		padding-bottom: 10px;
	}

	.section-header hr {
		width: calc(100% -2px);
		height: 4px;
		background-color: var(--color-primary);
		margin-top: 8px;
		margin: 0;
		position: sticky;
		top: 44px;
		z-index: 10;
	}
	.snap-scroll-bottom {
		scroll-snap-align: end;
	}
	.exit-anchor {
		height: 1px;
		position: absolute;
		bottom: 0;
	}
	.hand {
		display: inline-block;
		transform-origin: 70% 70%;
	}

	/* Triggered only when wave class is added */
	.wave {
		animation: wave-animation 1.8s ease-in-out 1 forwards;
		animation-fill-mode: forwards;
		animation-delay: 0.4s;
	}

	@keyframes wave-animation {
		0% {
			transform: rotate(1deg);
		}
		10% {
			transform: rotate(12deg);
		}
		20% {
			transform: rotate(-6deg);
		}
		30% {
			transform: rotate(12deg);
		}
		40% {
			transform: rotate(-2deg);
		}
		50% {
			transform: rotate(8deg);
		}
		60% {
			transform: rotate(1deg);
		}
		100% {
			transform: rotate(1deg);
		}
	}
</style>
