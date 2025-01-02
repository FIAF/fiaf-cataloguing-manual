
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive 

WORKDIR /manual

COPY . /manual

RUN apt update

RUN apt install -y pandoc \
    texlive-xetex

# RUN chmod +x /manual/test.sh

# ENTRYPOINT ["/manual/test.sh"]    
