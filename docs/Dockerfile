FROM node:22-alpine AS build

WORKDIR /app/docs

ARG PUBLIC_LANDING_URL=""
ARG PUBLIC_SITE_URL=""
ARG PUBLIC_REPO_URL=""
ARG PUBLIC_INSTALL_PACKAGE="ctxsift"

ENV NODE_ENV=production \
        PUBLIC_LANDING_URL=${PUBLIC_LANDING_URL} \
        PUBLIC_SITE_URL=${PUBLIC_SITE_URL} \
        PUBLIC_REPO_URL=${PUBLIC_REPO_URL} \
        PUBLIC_INSTALL_PACKAGE=${PUBLIC_INSTALL_PACKAGE}

RUN corepack enable && corepack prepare pnpm@11.3.0 --activate

COPY docs/package.json docs/pnpm-lock.yaml docs/pnpm-workspace.yaml ./

RUN pnpm install --frozen-lockfile

COPY docs/ ./
COPY benchmark/ ../benchmark/
COPY SKILL.md ../SKILL.md

RUN pnpm build

FROM docker.io/library/nginx:1.27-alpine AS runtime

COPY docs/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/docs/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
