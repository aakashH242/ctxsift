// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
    integrations: [
        starlight({
            title: 'CtxSift',
            description: 'Local-first command output compression and recall for coding agents.',
            tagline: 'Save tokens. Keep context. Recover state faster.',
            customCss: ['/src/styles/global.css'],
            titleDelimiter: '·',
            head: [
                {
                    tag: 'link',
                    attrs: { rel: 'icon', href: '/favicon.svg?v=2', type: 'image/svg+xml' },
                },
                {
                    tag: 'link',
                    attrs: { rel: 'icon', href: '/favicon.png?v=2', type: 'image/png', sizes: '512x512' },
                },
                {
                    tag: 'link',
                    attrs: { rel: 'apple-touch-icon', href: '/apple-touch-icon.png?v=2' },
                },
                {
                    tag: 'script',
                    attrs: { type: 'module' },
                    content: `
                        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                        mermaid.initialize({ startOnLoad: false, theme: 'dark' });
                        
                        async function renderMermaid() {
                            const containers = document.querySelectorAll('.expressive-code');
                            let hasMermaid = false;
                            for (const container of containers) {
                                const pre = container.querySelector('pre[data-language="mermaid"]');
                                if (!pre) continue;
                                hasMermaid = true;
                                
                                const copyBtn = container.querySelector('button[data-code]');
                                let content = '';
                                if (copyBtn && copyBtn.getAttribute('data-code')) {
                                    content = copyBtn.getAttribute('data-code').replace(/\u007f/g, '\\n');
                                } else {
                                    const lines = pre.querySelectorAll('.ec-line');
                                    if (lines.length > 0) {
                                        content = Array.from(lines).map(line => line.textContent).join('\\n');
                                    } else {
                                        content = pre.innerText || pre.textContent || '';
                                    }
                                }
                                
                                const div = document.createElement('div');
                                div.className = 'mermaid';
                                div.style.background = 'transparent';
                                div.style.display = 'flex';
                                div.style.justifyContent = 'center';
                                div.style.margin = '1.5rem 0';
                                div.textContent = content;
                                container.replaceWith(div);
                            }
                            if (hasMermaid) {
                                await mermaid.run();
                            }
                        }
                        
                        renderMermaid();
                        document.addEventListener('astro:page-load', renderMermaid);
                        document.addEventListener('astro:after-swap', renderMermaid);
                    `
                }
            ],
            sidebar: [
                {
                    label: 'Getting Started',
                    items: [
                        { label: 'Installation', slug: 'docs/getting-started/installation' },
                        { label: 'Configure', slug: 'docs/getting-started/configure' },
                        { label: 'Doctor', slug: 'docs/getting-started/doctor' },
                    ],
                },
                {
                    label: 'Concepts',
                    items: [
                        { label: 'Compress', slug: 'docs/concepts/compress' },
                        { label: 'Recall', slug: 'docs/concepts/recall' },
                        { label: 'Freshness', slug: 'docs/concepts/freshness' },
                    ],
                },
                {
                    label: 'Guides',
                    items: [
                        { label: 'Local Models', slug: 'docs/guides/local-models' },
                        { label: 'Remote Models', slug: 'docs/guides/remote-models' },
                        { label: 'Benchmark', slug: 'docs/guides/benchmark' },
                    ],
                },
                {
                    label: 'Blog',
                    items: [
                        { label: 'Blog Home', slug: 'docs/blog' },
                        { label: 'What Motivated CtxSift', slug: 'docs/blog/what-motivated-ctxsift' },
                        { label: 'Command-Output Recall: The Missing Layer After Compression', slug: 'docs/blog/command-output-recall' },
                    ],
                },
                {
                    label: 'Reference',
                    items: [
                        { label: 'CLI', slug: 'docs/reference/cli' },
                        { label: 'Config', slug: 'docs/reference/config' },
                        { label: 'Environment Variables', slug: 'docs/reference/env-vars' },
                    ],
                },
            ],
        }),
    ],

  vite: {
    plugins: [tailwindcss()],
  },
});