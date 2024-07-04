FROM alpine
WORKDIR /root
RUN apk update
RUN apk add git nodejs npm
RUN git clone https://github.com/alswl/dbml-editor /root
RUN npm install -g pnpm
RUN pnpm install
ENTRYPOINT ["pnpm", "start"]
