FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /home/app
WORKDIR /home/app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./paritetdent /home/app/

EXPOSE 8000
