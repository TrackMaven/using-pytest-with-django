FROM python:3.3

# Add etcdenv
ADD https://github.com/upfluence/etcdenv/releases/download/v0.3.1/etcdenv-linux-amd64-0.3.1 /usr/local/bin/etcdenv
RUN chmod +x /usr/local/bin/etcdenv

ADD requirements.txt /code/requirements.txt

WORKDIR /code/

RUN pip install -r requirements.txt
ADD requirements-dev.txt /code/requirements-dev.txt
RUN pip install -r requirements-dev.txt

ADD . /code