<script lang="ts">
	export let data;
	import PostEditor from '$lib/components/PostEditor.svelte';
</script>

<h1>Welcome, {JSON.stringify(data)}!</h1>
<PostEditor />
