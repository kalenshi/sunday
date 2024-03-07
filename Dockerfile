FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt

RUN apt-get update && \
    apt-get install -y git && \
    git init && \
    apt-get install -y vim && \
    apt-get install -y redis-tools && \
    apt-get install -y gcc python3-dev && \
    apt-get install -y libxml2-dev libxslt1-dev build-essential python3-lxml zlib1g-dev && \
    apt-get install -y default-mysql-client default-libmysqlclient-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0:8000"]
