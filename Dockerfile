# Pull base image
FROM resin/rpi-raspbian:jessie
MAINTAINER Amol Mundayoor <amol@smartthings.com>

# Install dependencies
RUN apt-get update && apt-get install -y \
    git-core \
    build-essential \
    gcc \
    python \
    python-dev \
    python-pip \
    python-virtualenv \
    python-rpi.gpio \
    python3-rpi.gpio \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*
RUN pip install pyserial
RUN git clone git://git.drogon.net/wiringPi
RUN cd wiringPi && ./build
RUN pip install wiringpi2

# Define working directory
WORKDIR /data
VOLUME /data

ADD ./wiringpi-test.py /data
ADD ./rpigpio-test.py /data

# Define default command
CMD ["bash"]
