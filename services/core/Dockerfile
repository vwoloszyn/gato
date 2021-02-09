FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code/
COPY . /code/
#COPY ../../helper /helper
#COPY requirements.txt /code/
RUN apt update
RUN apt-get install libgl1-mesa-glx -y
RUN pip3 install -r requirements.txt