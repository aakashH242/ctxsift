import type { APIRoute } from 'astro';

import { buildPowerShellInstaller, suggestedDownloadName } from '../../data/installer-scripts';

export const prerender = true;

export const GET: APIRoute = () => new Response(buildPowerShellInstaller(), {
  headers: {
    'Content-Type': 'text/plain; charset=utf-8',
    'Content-Disposition': `attachment; filename="${suggestedDownloadName('windows')}"`,
  },
});