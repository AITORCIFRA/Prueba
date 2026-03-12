FROM python:3.12-alpine

RUN apk add --no-cache \
    python3 \
    py3-pip \
    busybox \
    sqlite \
    sqlite-dev \
    ca-certificates \
    && ln -sf python3 /usr/bin/python

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

COPY . .

RUN chmod 0644 cron-jobs && crontab cron-jobs

CMD ["/usr/sbin/crond", "-f", "-L", "/dev/stdout"]