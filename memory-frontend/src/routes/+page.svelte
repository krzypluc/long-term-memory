<script lang="ts">
	import '../style.css';
	import axios from 'axios';
	import type { SearchResponse } from '../types/searchResponseData';
	import Tile from './Tile.svelte';

	let searchValue = '';

	let searchResponseData: SearchResponse;
	let promise = {};

	const handleSearchChange = () => {
		promise = axios.get('http://localhost:8000/search/' + searchValue).then(function (response) {
			searchResponseData = {
				data: response.data
			};
			console.log(searchResponseData);
		});
	};
</script>

<div class="columns pt-6">
	<div class="column is-6 is-offset-3">
		<input
			on:input|preventDefault={handleSearchChange}
			bind:value={searchValue}
			class="input p-5"
			type="text"
			placeholder="Search"
		/>
	</div>
</div>

<div class="columns">
	<div class="column is-6 is-offset-3 has-text-centered">
		{#await promise}
			<p class="element is-loading">Loading...</p>
		{:then response}
			<table class="table is-fullwidth is-bordered">
				<tbody>
					{#each searchResponseData.data as row}
						<tr>
							<Tile row={row}/>
						</tr>
					{/each}
				</tbody>
			</table>
		{:catch error}
			<div class="notification is-danger">
				<p>{error.message}</p>
			</div>
		{/await}
	</div>
</div>
