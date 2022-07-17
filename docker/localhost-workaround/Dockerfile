FROM ubuntu:22.04

RUN apt-get update \
   && apt-get install --no-install-recommends -y \
     nftables \
     python3 \
   && apt-get clean \
   && rm -rf /var/lib/apt/lists/*