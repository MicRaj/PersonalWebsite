<script lang="ts">
	import { browser } from '$app/environment';
	import { onMount, onDestroy } from 'svelte';
	import TinyEditor from './TinyEditor.svelte';

	let title: string = '';
	let cover_image_path: string = '';
	let content: string = '';

	function handleSubmit() {
		console.log('Submitted Title:', title);
		console.log('Submitted Cover Image:', cover_image_path);
		console.log('Submitted Content:', content);
		fetch('/api/posts/create_post', {
			method: 'POST',
			headers: {
				'Content-type': 'application/json; charset=UTF-8'
			},
			body: JSON.stringify({
				title: title,
				content: content,
				cover_image: cover_image_path
			})
		})
			.then((response) => response.json())
			.then((data) => {
				console.log('Response from server:', data);
			})
			.catch((error) => {
				console.error('Error submitting content:', error);
			});
	}
</script>

{#if browser}
	<div class="editor-container">
		<input type="text" bind:value={title} placeholder="Enter title" class="title-input" />
		<input
			type="text"
			bind:value={cover_image_path}
			placeholder="Enter cover image path"
			class="title-input"
		/>

		<TinyEditor bind:content />

		<button on:click={handleSubmit} class="submit-button">Submit</button>
	</div>
{:else}
	<p>Editor loading...</p>
{/if}

<style>
	.editor-container {
		max-width: 60%;
		margin: 2rem auto;
		padding: 1rem;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.title-input {
		padding: 0.5rem;
		font-size: 1.5rem;
		border: 1px solid #ccc;
		border-radius: 4px;
		width: 100%;
	}

	.submit-button {
		align-self: flex-start;
		padding: 0.6rem 1.2rem;
		font-size: 1rem;
		background-color: #007bff;
		color: white;
		border: none;
		border-radius: 4px;
		cursor: pointer;
	}

	.submit-button:hover {
		background-color: #0056b3;
	}

	:global(.tox) {
		max-width: 100%;
	}
</style>
