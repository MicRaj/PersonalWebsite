<script lang="ts">
	import { browser } from '$app/environment';
	import { onMount, onDestroy } from 'svelte';

	let editorId = 'my-tinymce-editor';
	let title: string = '';

	export let content: string = '';
	export let height: number = 300;

	let editorInstance: any;

	onMount(async () => {
		if (!browser) return;

		const tinymce = (await import('tinymce/tinymce')).default;

		await import('tinymce/icons/default');
		await import('tinymce/themes/silver');
		await import('tinymce/models/dom');
		await import('tinymce/plugins/link');
		await import('tinymce/plugins/lists');

		tinymce.init({
			selector: `#${editorId}`,
			license_key: 'gpl',
			height,
			menubar: false,
			branding: false,
			statusbar: false,
			plugins: ['advlist', 'autolink', 'lists', 'link', 'image', 'wordcount'],
			toolbar:
				'undo redo | blocks fontfamily fontsize| ' +
				'bold italic backcolor | alignleft aligncenter ' +
				'alignright alignjustify | bullist numlist outdent indent | ',
			content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:16px }',
			skin_url: '/tinymce/skins/ui/oxide',
			content_css: '/tinymce/skins/content/default/content.css',
			base_url: '/tinymce',
			setup(editor) {
				editor.on('Change KeyUp', () => {
					content = editor.getContent();
				});
				editor.setContent(content);
				editorInstance = editor;
			}
		});
	});

	onDestroy(() => {
		if (browser && editorInstance) {
			import('tinymce').then(({ default: tinymce }) => {
				tinymce.remove(editorInstance);
			});
		}
	});

	function handleSubmit() {
		console.log('Submitted Title:', title);
		console.log('Submitted Content:', content);
		fetch('http://127.0.0.1:8000/posts/create_post', {
			method: 'POST',
			headers: {
				'Content-type': 'application/json; charset=UTF-8'
			},
			body: JSON.stringify({
				title: title,
				content: content
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

		<textarea id={editorId}></textarea>

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
