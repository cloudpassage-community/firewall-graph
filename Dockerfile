FROM alpine:3.4
MAINTAINER toolbox@cloudpassage.com

RUN apk add -U \
    python \
    py-pip

COPY ./ /app/

WORKDIR /app/

RUN pip install -e .

RUN py.test --cov=firewallgraph
