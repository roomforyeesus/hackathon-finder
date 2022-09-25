FROM node:16.13.0-alpine3.14 as build

WORKDIR /frontend
COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./
RUN npm install
COPY ./frontend/ ./
RUN npm run build


FROM nginx:1.21.1-alpine

COPY ./nginx/nginx-setup.conf /etc/nginx/conf.d/default.conf
COPY --from=build /frontend/dist /usr/share/nginx/html