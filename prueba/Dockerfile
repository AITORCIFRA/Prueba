FROM node:20-alpine

RUN apk add --no-cache \
    python3 \
    py3-pip \
    dcron \
    sqlite \
    sqlite-dev \
    ca-certificates \
    && ln -sf python3 /usr/bin/python

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt --break-system-packages

COPY package*.json ./
RUN npm install

COPY . .

RUN chmod 0644 crontab && crontab crontab

EXPOSE 3000

CMD ["sh", "-c", "crond && npm run dev"]