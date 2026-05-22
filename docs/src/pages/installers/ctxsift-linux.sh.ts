import type { APIRoute } from 'astro';

import { buildUnixInstaller, suggestedDownloadName } from '../../data/installer-scripts';

export const prerender = true;

export const GET: APIRoute = () => new Response(buildUnixInstaller('linux'), {
  headers: {
    'Content-Type': 'text/x-shellscript; charset=utf-8',
    'Content-Disposition': `attachment; filename="${suggestedDownloadName('linux')}"`,
  },
});