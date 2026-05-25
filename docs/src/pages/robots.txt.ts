import type { APIRoute } from 'astro';

function siteBaseUrl(): string {
  const explicit = process.env.PUBLIC_SITE_URL || process.env.PUBLIC_LANDING_URL || 'https://ctxsift.dev';
  return explicit.replace(/\/+$/, '');
}

export const GET: APIRoute = () => {
  const body = [
    'User-agent: *',
    'Allow: /',
    `Sitemap: ${siteBaseUrl()}/sitemap-index.xml`,
    '',
  ].join('\n');

  return new Response(body, {
    headers: {
      'Content-Type': 'text/plain; charset=utf-8',
      'Cache-Control': 'public, max-age=300',
    },
  });
};
