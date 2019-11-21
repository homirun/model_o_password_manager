FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src

ADD requirements.txt /src/
RUN apk add gcc build-base linux-headers bash mariadb-dev nodejs npm
RUN pip install --no-cache-dir -r /src/requirements.txt
ADD . /src/
