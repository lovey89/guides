FROM ubuntu:22.04

WORKDIR /root

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
       software-properties-common \
       ca-certificates \
       gnupg2 \
       # For video codecs
       libavcodec58 \
       pulseaudio && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN add-apt-repository -y ppa:mozillateam/ppa && \
    /bin/echo -e "Package: *\nPin: release o=LP-PPA-mozillateam\nPin-Priority: 1001" | tee /etc/apt/preferences.d/mozilla-firefox && \
    apt-get update && \
    apt-get install --no-install-recommends -y \
      firefox && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*