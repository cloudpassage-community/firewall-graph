FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.0.6
MAINTAINER toolbox@cloudpassage.com


RUN apt-get update && apt-get install -y \
    gcc\
    graphviz \
    graphviz-dev \
    linux-headers-generic

COPY ./ /app/

WORKDIR /app/

RUN pip install \
    pytest \
    pytest-cov \
    pytest-flake8 \
    codeclimate-test-reporter==0.2.0

RUN pip install \
    pygraphviz==1.4rc1 --install-option="--include-path=/usr/include/graphviz" --install-option="--library-path=/usr/lib/graphviz/"


RUN pip install -e .

RUN py.test -v --cov-report term-missing --cov=firewallgraph

CMD python /app/application.py

########################################

FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.0.6
MAINTAINER toolbox@cloudpassage.com

ENV HALO_API_HOSTNAME=api.cloudpassage.com

RUN apt-get update && apt-get install -y \
    gcc\
    graphviz \
    graphviz-dev \
    linux-headers-generic

COPY ./ /app/

WORKDIR /app/

RUN pip install \
    pygraphviz==1.4rc1 --install-option="--include-path=/usr/include/graphviz" --install-option="--library-path=/usr/lib/graphviz/"


RUN pip install -e .

CMD python /app/application.py
