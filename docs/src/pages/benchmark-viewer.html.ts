import { access, readFile } from 'node:fs/promises';
import { resolve } from 'node:path';

import type { APIRoute } from 'astro';

export const prerender = true;

const latestViewerPath = resolve(process.cwd(), '..', 'benchmark', 'results', 'viewer.html');

function missingViewerPage(): string {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Benchmark Viewer Not Generated</title>
  <style>
    :root { color-scheme: dark; }
    body {
      margin: 0;
      font-family: system-ui, sans-serif;
      background: #06111d;
      color: #e5eef8;
      min-height: 100vh;
      display: grid;
      place-items: center;
      padding: 24px;
    }
    main {
      max-width: 760px;
      background: #0c1b2b;
      border: 1px solid #1d3550;
      border-radius: 18px;
      padding: 28px;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.25);
    }
    h1 { margin-top: 0; font-size: 1.8rem; }
    p, li { line-height: 1.65; color: #bfd0e2; }
    code {
      font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
      background: #08131f;
      padding: 0.15rem 0.35rem;
      border-radius: 6px;
    }
  </style>
</head>
<body>
  <main>
    <h1>Benchmark viewer not generated yet</h1>
    <p>The docs route exists, but the current checkout does not have a generated <code>benchmark/results/viewer.html</code> snapshot to serve.</p>
    <p>Generate it locally with:</p>
    <pre><code>uv run python -m benchmark.viewer ./benchmark/results/</code></pre>
    <p>Then rebuild the docs site to publish the latest static snapshot here.</p>
  </main>
</body>
</html>`;
}

export const GET: APIRoute = async () => {
  try {
    await access(latestViewerPath);
  } catch {
    return new Response(missingViewerPage(), {
      headers: {
        'Content-Type': 'text/html; charset=utf-8',
      },
    });
  }

  const html = await readFile(latestViewerPath, 'utf-8');
  return new Response(html, {
    headers: {
      'Content-Type': 'text/html; charset=utf-8',
    },
  });
};