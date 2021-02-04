FROM python:3.8

WORKDIR /app/Gamein/

RUN apt update && apt install -y vim curl gettext

COPY requirements.txt /app/dbproject
ENV PIP_NO_CACHE_DIR 1
RUN pip install -r requirements.txt

COPY . .
