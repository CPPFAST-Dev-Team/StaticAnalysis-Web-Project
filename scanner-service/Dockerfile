ARG NODE_VERSION=22.10.0
ARG SEMGREP_SHA=b616773

FROM docker.io/library/node:${NODE_VERSION}-alpine AS node

RUN mkdir /app
WORKDIR /app
COPY package.json package.json
COPY package-lock.json package-lock.json
RUN npm install
COPY src/ src/
COPY tsconfig.json tsconfig.json
RUN npm run build

FROM docker.io/semgrep/semgrep:sha-${SEMGREP_SHA}

COPY --from=node /usr/lib /usr/lib
COPY --from=node /usr/local/lib /usr/local/lib
COPY --from=node /usr/local/include /usr/local/include
COPY --from=node /usr/local/bin /usr/local/bin
COPY --from=node /app/node_modules /scanner/node_modules
COPY --from=node /app/dist /scanner

WORKDIR /scanner
COPY entry.sh entry.sh
RUN chmod +x entry.sh

ENTRYPOINT [ "/scanner/entry.sh" ]