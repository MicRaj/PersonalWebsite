<script lang="ts">
	import { goto } from '$app/navigation';

	interface LoginPageData {
		next?: string;
	}
	export let data: LoginPageData;

	let username = '';
	let password = '';
	let loading = false;
	let error = '';

	async function handleLogin() {
		loading = true;
		error = '';
		try {
			const res = await fetch('/api/login/', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ username, password }),
				credentials: 'include'
			});

			if (!res.ok) {
				const result = await res.json();
				error = result.message || 'Login failed';
			} else {
				const next = data.next || '/';
				goto(next);
			}
		} catch (e) {
			error = 'Network error';
		} finally {
			loading = false;
		}
	}
</script>

<main class="login-container">
	<h1>Login</h1>
	{#if error}
		<div class="error">{error}</div>
	{/if}
	<form on:submit|preventDefault={handleLogin}>
		<label>
			Username:
			<input type="text" bind:value={username} required />
		</label>
		<label>
			Password:
			<input type="password" bind:value={password} required />
		</label>
		<button type="submit" disabled={loading}>
			{#if loading}Logging in...{/if}
			{#if !loading}Login{/if}
		</button>
	</form>
</main>

<style>
	.login-container {
		max-width: 400px;
		margin: 2rem auto;
		padding: 2rem;
		border-radius: 8px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
		background: #fff;
	}
	label {
		display: block;
		margin-bottom: 1rem;
	}
	input {
		width: 100%;
		padding: 0.5rem;
		margin-top: 0.25rem;
		box-sizing: border-box;
	}
	button {
		width: 100%;
		padding: 0.75rem;
		background: #0070f3;
		color: #fff;
		border: none;
		border-radius: 4px;
		font-size: 1rem;
		cursor: pointer;
	}
	button:disabled {
		background: #aaa;
		cursor: not-allowed;
	}
	.error {
		color: #d00;
		margin-bottom: 1rem;
	}
</style>
