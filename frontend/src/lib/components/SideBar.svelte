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
</aside>

<style>
	/* When screen width is small */
	@media (max-width: 600px) {
		.sidebar {
			display: none;
		}
	}
	.sidebar {
		width: 175px;
		height: 100vh;
		position: relative; /* Needed for ::before positioning */
		/* Remove the full-height border */
	}
	.sidebar nav {
		padding: 5px;
	}
	.sidebar::before {
		content: '';
		position: absolute;
		top: 5%; /* space from the top */
		bottom: 5%; /* space from the bottom */
		right: 0;
		width: 7px;
		background-color: rgba(136, 150, 150, 0.5); /* or #000000 if you prefer */
		border-radius: 10px;
	}

	/* Sidebar */
	ul {
		list-style: none;
		padding: 125px 0px 0px 10px;
		line-height: 2.5;
	}

	li a {
		text-decoration: none;
		color: #14080e;
		font-weight: 500;
		padding-left: 10px;
		border-left: 4px solid transparent;
		transition: border-color 0.3s ease;
		font-family: 'Space Grotesk', sans-serif;
		font-size: 1.5rem;
		font-weight: 700;
	}

	li a:hover {
		color: #6ca6c1;
	}

	li a.selected {
		border-left-color: #6ca6c1; /* Active left border */
		color: #6ca6c1;
		font-weight: 700;
	}

	.social-icons img {
		width: 24px;
		margin: 10px 0;
		cursor: pointer;
	}
</style>
