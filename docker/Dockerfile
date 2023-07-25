FROM python:3.10.5-buster

COPY . /app
WORKDIR /app

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV DEBIAN_FRONTEND="noninteractive"
ENV TZ=America/Sao_Paulo

RUN python -m pip install --upgrade pip \
    pip install -r requirements.txt \
    && pip install uwsgi \
    && apt-get install -y tzdata \
    && apt-get install -y --no-install-recommends
