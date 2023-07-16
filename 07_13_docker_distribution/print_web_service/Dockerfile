FROM ubuntu:latest
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
LABEL maintainer "yumjunstar <yumjunstar@naver.com>"

RUN apt update && apt install -yq python3 python3-pip net-tools
RUN ifconfig
WORKDIR /app

COPY app.py /app
COPY requirements.txt /app

RUN pip3 install -r requirements.txt

CMD ["bash", "-c", "ifconfig -a && python3 app.py"]