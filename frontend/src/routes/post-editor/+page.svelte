<script lang="ts">
	export let data;
	import PostEditor from '$lib/components/PostEditor.svelte';
</script>

<h1>Welcome, {data.user.username}!</h1>
<PostEditor />
