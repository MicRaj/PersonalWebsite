<script lang="ts">
	export let sections: string[] = [];

	import { onMount, onDestroy } from 'svelte';
	import { writable } from 'svelte/store';

	let activeSection = writable(sections[0] || '');

	function handleClick(event: MouseEvent) {
		event.preventDefault();

		const target = event.currentTarget as HTMLAnchorElement;
		const href = target.getAttribute('href');

		if (!href) return;

		const targetId = href.substring(1);
		const targetSection = document.getElementById(targetId);

		if (targetSection) {
			targetSection.scrollIntoView({ behavior: 'smooth' });
			// activeSection.set(targetId);
		}
	}

	let observer: IntersectionObserver;

	onMount(() => {
		const options = {
			root: null,
			rootMargin: '0px',
			threshold: 0.1 // Adjust how much should be visible to be "active"
		};

		observer = new IntersectionObserver((entries) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					activeSection.set(entry.target.id);
				}
			});
		}, options);

		sections.forEach((sectionId) => {
			const el = document.getElementById(sectionId);
			if (el) observer.observe(el);
		});
	});

	onDestroy(() => {
		if (observer) observer.disconnect();
	});
</script>

<aside class="sidebar">
	<nav>
		<ul>
			{#each sections as section}
				<li>
					<a
						href={`#${section}`}
						on:click={handleClick}
						class:selected={$activeSection === section}
					>
						{section.charAt(0).toUpperCase() + section.slice(1)}
					</a>
				</li>
			{/each}
		</ul>
	</nav>
	<!-- Social Icons -->
	<div class="social-icons">
		<a
			href="https://github.com/your-username"
			target="_blank"
			rel="noopener noreferrer"
			aria-label="GitHub"
		>
			<img src="/icons/github_icon.svg" alt="GitHub" />
		</a>
		<a
			href="https://linkedin.com/in/your-username"
			target="_blank"
			rel="noopener noreferrer"
			aria-label="LinkedIn"
		>
			<img src="/icons/linkedin_icon.svg" alt="LinkedIn" />
		</a>
	</div>
</aside>

<style>
	/* When screen width is small */
	@media (max-width: 768px) {
		.sidebar {
			display: none;
		}
	}
	.sidebar {
		width: 200px;
		height: 100vh;
		position: relative;
		user-select: none;
	}
	.sidebar::before {
		content: '';
		position: absolute;
		top: 20px; /* space from the top */
		bottom: 20px; /* space from the bottom */
		right: 0;
		width: 7px;
		background-color: var(--color-accent); /* or #000000 if you prefer */
		border-radius: 10px;
	}

	/* Sidebar */
	ul {
		list-style: none;
		padding: 125px 0px 0px 10px;
		line-height: 2.5;
		margin: 0;
	}

	li a {
		text-decoration: none;
		color: var(--color-secondary-text);
		font-weight: 500;
		border-left: 4px solid transparent;
		padding-left: 30px;
		transition: border-color 0.3s ease;
		font-family: var(--font-heading);
		font-size: 1.5rem;
		font-weight: 700;
		cursor: pointer;
	}

	li a:hover {
		color: var(--color-primary);
	}

	li a.selected {
		border-left-color: var(--color-primary);
		color: var(--color-primary);
		font-weight: 700;
	}

	.social-icons {
		position: relative;
		top: clamp(100px, 20vh, 400px);
		display: flex;
		flex-direction: row;
		gap: 24px;
		z-index: 1000;
		width: 100%;
		justify-content: center;
	}

	.social-icons a img {
		cursor: pointer;
		width: 50px;
		height: 50px;
	}
</style>
