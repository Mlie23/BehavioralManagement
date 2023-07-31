FROM node:16-alpine as build

WORKDIR /app/frontend
RUN npm install --global serve
COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./
RUN npm ci --silent
COPY ./frontend/ ./
EXPOSE 8080
USER node
CMD [ "serve", "-s", "dist" ]