FROM node:14

WORKDIR /app

COPY package*.json ./
RUN apt-get update

RUN npm install

COPY . .

CMD ["node", "index.js"]
#CMD ["npm", "start"]
