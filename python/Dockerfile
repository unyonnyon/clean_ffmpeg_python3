FROM python:3.8-slim

ENV DEBCONF_NOWARNINGS yes

RUN apt-get update \
    && apt-get install -y wget \
    xz-utils \
    tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget http://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz \
    && tar Jxvf ffmpeg-release-amd64-static.tar.xz

ENV PATH=/ffmpeg-4.4-amd64-static:$PATH

ENV TZ=Azia/Tokyo

RUN useradd --uid 1000 -m python

WORKDIR /home/python/app

USER python

ENV PATH=/home/python/.local/bin:$PATH

COPY ./Pipfile* ./

RUN pip install pipenv \
    && pipenv sync --dev
