export type CompressionShowcase = {
  id: string;
  title: string;
  domain: string;
  intent: string;
  command: string;
  rawTokens: number;
  outputTokens: number;
  savedTokens: number;
  compressionRatio: number;
  rawPreview: string;
  compressedOutput: string;
  sourceLabel: string;
};

type CompressionShowcaseInput = Omit<
  CompressionShowcase,
  'savedTokens' | 'compressionRatio'
>;

function createCompressionShowcase(
  input: CompressionShowcaseInput,
): CompressionShowcase {
  const savedTokens = Math.max(input.rawTokens - input.outputTokens, 0);
  const compressionRatio =
    input.rawTokens > 0
      ? Math.round((savedTokens / input.rawTokens) * 1000) / 10
      : 0;
  return {
    ...input,
    savedTokens,
    compressionRatio,
  };
}

export const compressionShowcases: CompressionShowcase[] = [
  createCompressionShowcase({
    id: 'git-push-rejected',
    title: 'Push rejection recall',
    domain: 'git',
    intent: 'recall',
    command: 'git push origin main',
    rawTokens: 175,
    outputTokens: 35,
    rawPreview: `$ git push origin main
...
To https://github.com/example/mono-app.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/example/mono-app.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes before pushing again.`,
    compressedOutput:
      "git push origin main was rejected with main -> main (non-fast-forward) and error: failed to push some refs to 'https://github.com/example/mono-app.git'",
    sourceLabel:
      'Source: benchmark fixture git-02 and stored CtxSift output',
  }),
  createCompressionShowcase({
    id: 'docker-build-missing-entrypoint',
    title: 'Docker build failure recall',
    domain: 'docker',
    intent: 'recall',
    command: 'docker build -t api:dev .',
    rawTokens: 425,
    outputTokens: 79,
    rawPreview: `$ docker build -t api:dev .
...
#9 [5/6] COPY docker/entrypoint.sh /entrypoint.sh
#9 ERROR: failed to calculate checksum of ref 1f3d3b8a9e2e::9ng9it1k3b: "/docker/entrypoint.sh": not found
------
 > [5/6] COPY docker/entrypoint.sh /entrypoint.sh:
------
Dockerfile:14`,
    compressedOutput:
      'docker build -t api:dev . failed at Dockerfile:14 on COPY docker/entrypoint.sh /entrypoint.sh because /docker/entrypoint.sh not found; error: failed to solve: failed to calculate checksum of ref 1f3d3b8a9e2e::9ng9it1k3b: "/docker/entrypoint.sh": not found',
    sourceLabel:
      'Source: benchmark fixture docker-01 and stored CtxSift output',
  }),
  createCompressionShowcase({
    id: 'make-integration-migration-miss',
    title: 'Integration failure summary',
    domain: 'mixed',
    intent: 'summary',
    command: 'make integration',
    rawTokens: 137,
    outputTokens: 27,
    rawPreview: `$ make integration
[stdout] running migrations
[stdout] applying 202605010915_add_accounts_table.sql
[stdout] applying 202605071130_add_tokens_table.sql
[stderr] warning: locale not set, falling back to C.UTF-8
[stderr] psql:migrations/202605121045_add_login_audit.sql: No such file or directory
make: *** [integration] Error 2`,
    compressedOutput:
      'make integration failed with Error 2 because psql could not find the file migrations/202605121045_add_login_audit.sql.',
    sourceLabel:
      'Source: benchmark fixture mixed-02 and stored CtxSift output',
  }),
];
