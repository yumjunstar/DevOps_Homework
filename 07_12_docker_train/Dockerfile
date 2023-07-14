FROM tensorflow/tensorflow:latest
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
LABEL maintainer "yumjunstar <yumjunstar@naver.com>"
RUN apt-get update && apt-get -y install libgl1-mesa-glx
COPY app /app
COPY requirements.txt /app/
# COPY data /app/data
WORKDIR /app
RUN pip3 install -r requirements.txt


COPY train.py .

ENTRYPOINT [ "python" ]
CMD ["train.py"]
#docker run -it -v C:\Users\067\Desktop\DevOps\homework\3_docker_train\data:/app/data  tf_trainfile



# FROM ubuntu:22.04
# ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
# LABEL maintainer "yumjunstar <yumjunstar@naver.com>"
# RUN apt-get update
# RUN apt-get -yq install python3 python3-pip wget
# RUN wget https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Linux-x86_64.sh
# RUN bash Anaconda3-2023.07-1-Linux-x86_64.sh -b -p /opt/anaconda
# ENV PATH="/opt/anaconda/bin:${PATH}"
# #RUN /opt/anaconda/bin/conda init powershell

# COPY app /app
# COPY requirements.txt /app/
# COPY data /app/data
# WORKDIR /app
# #RUN /opt/anaconda/bin/conda env create -f requirements.yaml --name tf_env
# #RUN pip3 install -r requirements.txt


# COPY train.py .

# ENTRYPOINT [ "python3" ]
# CMD ["train.py"]