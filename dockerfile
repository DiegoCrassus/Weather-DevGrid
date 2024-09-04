FROM ubuntu:20.04
RUN mkdir /code
WORKDIR /code

RUN apt-get update

RUN apt-get install --fix-missing -y \
    curl \
    python3 \
    python3-pip \
    python3-setuptools \
    && rm -rf /var/lib/apt/lists/*  && \
    apt-get purge --auto-remove && \
    apt-get clean


COPY requirements.txt /code

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --upgrade flask-cors

COPY . /code

RUN chmod -R +x /code/

ENTRYPOINT ["gunicorn", "-c", "/code/src/api/config.py", "src:app", "--preload"]
