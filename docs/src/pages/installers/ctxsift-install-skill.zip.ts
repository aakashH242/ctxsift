import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import type { APIRoute } from 'astro';

import { buildSingleFileZip } from '../../data/zip-utils';

const DOWNLOAD_NAME = 'ctxsift-install-skill.zip';
const ARCHIVE_PATH = 'ctxsift-install/SKILL.md';

async function readRootSkillMarkdown(): Promise<string> {
  const skillPath = resolve(process.cwd(), '..', 'SKILL.md');
  return readFile(skillPath, 'utf-8');
}

export const GET: APIRoute = async () => {
  const content = await readRootSkillMarkdown();
  const zipBytes = buildSingleFileZip(ARCHIVE_PATH, Buffer.from(content, 'utf-8'));

  return new Response(Buffer.from(zipBytes), {
    headers: {
      'Content-Type': 'application/zip',
      'Content-Disposition': `attachment; filename="${DOWNLOAD_NAME}"`,
      'Cache-Control': 'public, max-age=300',
    },
  });
};
