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
    id: 'systemd-config-restart-loop',
    title: 'Service restart-loop summary',
    domain: 'systemd',
    intent: 'summary',
    command: 'systemctl restart api.service',
    rawTokens: 430,
    outputTokens: 25,
    rawPreview: `$ systemctl restart api.service
Job for api.service failed because the control process exited with error code.
See "systemctl status api.service" and "journalctl -u api.service -n 50" for details.
$ systemctl status api.service --no-pager
* api.service - HTTP API
May 16 11:27:40 buildbox api-server[21871]: {"level":"error","msg":"parse config","file":"/etc/api/config.yaml","line":17,"error":"yaml: unmarshal errors: line 17: field timeuot not found in type config.Server"}
May 16 11:27:41 buildbox systemd[1]: api.service: Start request repeated too quickly.`,
    compressedOutput:
      'api.service fails due to a config error at /etc/api/config.yaml line 17: unexpected field "timeuot".',
    sourceLabel:
      'Source: benchmark fixture systemd-02 and latest remote gpt-4.1 benchmark output',
  }),
  createCompressionShowcase({
    id: 'git-clone-connection-reset',
    title: 'Clone failure recall',
    domain: 'git',
    intent: 'recall',
    command: 'git clone --progress https://github.com/example/very-large-repo.git',
    rawTokens: 461,
    outputTokens: 32,
    rawPreview: `$ git clone --progress https://github.com/example/very-large-repo.git
Cloning into 'very-large-repo'...
remote: Enumerating objects: 248731, done.
remote: Compressing objects: 100% (84791/84791), done.
Receiving objects:  64% (159188/248731), 125.01 MiB | 210.00 KiB/s
error: RPC failed; curl 56 Recv failure: Connection reset by peer
fetch-pack: unexpected disconnect while reading sideband packet
fatal: early EOF
fatal: fetch-pack: invalid index-pack output`,
    compressedOutput:
      'git clone --progress https://github.com/example/very-large-repo.git failed with curl 56 Connection reset by peer and fetch-pack: invalid index-pack output',
    sourceLabel:
      'Source: benchmark fixture git-03 and latest remote gpt-4.1 benchmark output',
  }),
  createCompressionShowcase({
    id: 'compose-app-exit-after-migrations',
    title: 'Compose startup recall',
    domain: 'docker-compose',
    intent: 'recall',
    command: 'docker compose up --build',
    rawTokens: 364,
    outputTokens: 28,
    rawPreview: `$ docker compose up --build
[+] Running 3/3
[ok] Network demo_default     Created
[ok] Container demo-db-1      Created
[ok] Container demo-app-1     Created
db-1   | database system is ready to accept connections
app-1  | applying migrations
app-1  | ERROR sqlalchemy.exc.ProgrammingError: relation "tenant_settings" does not exist
app-1 exited with code 1
Aborting on container exit...`,
    compressedOutput:
      'docker compose up --build, demo-app-1, tenant_settings, sqlalchemy.exc.ProgrammingError, app-1 exited with code 1',
    sourceLabel:
      'Source: benchmark fixture docker-compose-02 and latest remote gpt-4.1 benchmark output',
  }),
];
