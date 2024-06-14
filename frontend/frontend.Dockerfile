FROM node:slim

WORKDIR /goald-frontend

RUN apt-get update && apt-get install --no-install-recommends -y \
    nodejs  \
    npm     \
&& rm -rf /var/lib/apt/lists/*

COPY . .

RUN npm install
RUN npm run build

CMD npm run srv
