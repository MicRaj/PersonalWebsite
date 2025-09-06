import type { PageServerLoad } from './$types';

export const load: PageServerLoad = ({ url }) => {
	return {
		next: url.searchParams.get('next') ?? '/'
	};
};
