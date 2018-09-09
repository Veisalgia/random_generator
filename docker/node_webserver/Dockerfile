# specify the node base image with your desired version node:<version>
FROM node:6
# replace this with your application's default port
WORKDIR /usr/src/app

COPY package*.json ./

EXPOSE 3000

COPY . .


RUN npm install


CMD [ "npm", "start" ]