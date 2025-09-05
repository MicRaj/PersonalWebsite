import { redirect } from '@sveltejs/kit';

export async function load({ fetch, url }) {
	const res = await fetch('http://backend:3000/me', {
		credentials: 'include' // important: send cookies
	});

	// if (res.status === 401) {
	// 	// throw redirect(302, `/login?next=${url.pathname}`);
	// }

	const user = await res.json();
	return { user };
}
