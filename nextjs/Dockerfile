FROM docker.io/library/node:20.13.1

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build

ENV PORT 3000
CMD ["./node_modules/.bin/next", "start", "-p", ${PORT}]
