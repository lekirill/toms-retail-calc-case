FROM node:lts-alpine

WORKDIR /app

COPY ./app/package.json /app/package.json
COPY ./app/package-lock.json /app/package-lock.json
RUN npm install
RUN npm install axios

COPY ./app /app

CMD npm run serve