FROM ubuntu:latest
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
LABEL maintainer "yumjunstar <yumjunstar@naver.com>"

RUN apt update && apt install -yq python3 python3-pip
WORKDIR /app

COPY data /app
COPY requirements.txt /app
COPY calculation.py /app
RUN pip3 install -r requirements.txt


ENTRYPOINT [ "python3", "calculation.py" ]


# #FROM tensorflow/tensorflow:latest
# ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
# LABEL maintainer "yumjunstar <yumjunstar@naver.com>"
# RUN apt-get update && apt-get -y install libgl1-mesa-glx
# COPY app /app
# COPY requirements.txt /app/
# # COPY data /app/data
# WORKDIR /app
# RUN pip3 install -r requirements.txt


# COPY train.py .

# ENTRYPOINT [ "python" ]
# CMD ["train.py"]
# #docker run -it -v C:\Users\067\Desktop\DevOps\homework\3_docker_train\data:/app/data  tf_trainfile