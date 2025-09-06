import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch, cookies, url }) => {
	const sessionId = cookies.get('session_id');

	const res = await fetch('http://backend:3000/me', {
		headers: {
			cookie: `session_id=${sessionId}`
		}
	});

	if (res.status === 401) {
		const next = encodeURIComponent(url.pathname + url.search);
		throw redirect(302, `/login?next=${next}`);
	}

	const user = await res.json();
	return { user };
};
