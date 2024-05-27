FROM docker.io/library/node:20.13.1

WORKDIR /app

COPY . .

RUN ls -l