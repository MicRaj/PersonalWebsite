<script lang="ts">
	import { browser } from '$app/environment';
	import { onMount, onDestroy } from 'svelte';

	let editorId = 'my-tinymce-editor';

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
</script>

<textarea id={editorId}></textarea>
