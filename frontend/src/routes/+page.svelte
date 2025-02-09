<script lang="ts">
	import { onMount } from 'svelte';

	type Answer = {
		id: Number;
		timestamp: String;
		answer: String;
	};

	let imageSrc = '/hamster_neutral.jpg';
	let answers: Answer[] = [];

	async function getAnswers() {
		try {
			const response = await fetch('/api/get');
			const data = await response.json();
			console.log(data);
			answers = data;
		} catch (error) {
			console.error('Error getting answers:', error);
		}
	}

	async function handleYesClick() {
		imageSrc = '/hamster_happy.jpg';
		try {
			await fetch('/api/upload', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: 'Yes'
			});
		} catch (error) {
			console.error('Error uploading response:', error);
		}
		getAnswers();
	}

	async function handleNoClick() {
		imageSrc = '/hamster_angry.jpg';
		try {
			await fetch('/api/upload', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: 'No'
			});
		} catch (error) {
			console.error('Error uploading response:', error);
		}
		getAnswers();
	}
	// Fetch answers when the component mounts
	onMount(() => {
		getAnswers();
	});
</script>

<div class="container">
	<!-- Image Section -->
	<div>
		<!-- <img src={imageSrc} alt="Hamster" /> -->
	</div>

	<!-- Button Section with Paragraph -->
	<div class="button-section">
		<button class="yes" on:click={handleYesClick}>YES</button>
		<p>yes or no?</p>
		<button class="no" on:click={handleNoClick}>NO</button>
	</div>
	<table class="answers-table">
		<thead>
			<tr>
				<th>ID</th>
				<th>Answer</th>
				<th>Timestamp</th>
			</tr>
		</thead>
		<tbody>
			{#each answers.slice().reverse() as answer}
				<tr>
					<td>{answer.id}</td>
					<td>{answer.answer}</td>
					<td>{answer.timestamp}</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>

<style>
	.container {
		margin-top: 2rem;
		text-align: center;
	}

	.button-section {
		margin-top: 1.5rem;
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 1rem;
	}

	img {
		max-width: 100%;
		height: auto;
	}

	button {
		padding: 0.5rem 1.5rem;
		font-size: 1rem;
		border: none;
		border-radius: 0.25rem;
		cursor: pointer;
	}

	button.yes {
		background-color: #0d6efd;
		color: white;
	}

	button.no {
		background-color: #6c757d;
		color: white;
	}

	.answers-table {
		width: 100%;
		border-collapse: collapse;
		margin-top: 1rem;
	}

	.answers-table th,
	.answers-table td {
		border: 1px solid #ddd;
		padding: 10px;
		text-align: left;
	}

	.answers-table th {
		background-color: #0d6efd;
		color: white;
	}

	.answers-table tr:nth-child(even) {
		background-color: #f8f9fa;
	}

	.answers-table tr:hover {
		background-color: #e2e6ea;
	}
</style>
