FROM node:20.3.0-slim

# RUN mkdir -p workspace
WORKDIR /app

COPY ./package.json ./

RUN npm install

COPY . .

EXPOSE 3001

CMD ["npm", "start"]