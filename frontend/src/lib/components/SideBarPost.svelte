<script lang="ts">
	import { goto } from '$app/navigation';

	function goHome() {
		goto('/');
	}
</script>

<aside class="sidebar">
	<!-- Back to Home Button -->
	<nav>
		<ul>
			<li>
				<a on:click={goHome}>Back</a>
			</li>
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
	/* Hide sidebar on small screens */
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

	.social-icons {
		position: relative;
		top: 100px;
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
		transition: transform 0.2s ease;
	}

	.social-icons a img:hover {
		transform: scale(1.1);
	}
</style>
