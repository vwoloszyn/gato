FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code/
COPY . /code/
#COPY ../../helper /helper
#COPY requirements.txt /code/
RUN apt-get update 
#&& apt-get install -y swig
RUN apt-get install -y libpulse-dev
RUN apt-get install -y swig
RUN apt-get install -y portaudio19-dev python-pyaudio python3-pyaudio
RUN apt-get install -y libasound2-dev
RUN apt-get install -y alsa-utils
#RUN  apt-get install fglrx -y
RUN pip3 install -r requirements.txt