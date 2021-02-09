FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code/
COPY . /code/
#COPY ../../helper /helper
#COPY requirements.txt /code/
RUN pip3 install -r requirements.txt


# FROM python:3

# ENV PYTHONUNBUFFERED 1

# ENV APP_ROOT /
# ENV ALLOWED_HOSTS "web,.tu-berlin.de,130.149.222.199,open-science.berlin,localhost,127.0.0.1"
# ENV LOG_FILE_PATH "/var/log/django/webapp_django6.log"
# ENV LOG_FILE_DIR "/var/log/django"
# ENV PATH="${APP_ROOT}:${PATH}"

# #extra packges
# RUN apt-get update -y
# #RUN apt-get install -y python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev libpulse-dev swig
# #RUN apt-get install -y python-dev 
# RUN apt-get install python3
# RUN pip3 install django
# # install prerequisites
# #RUN pip install pipenv

# RUN mkdir /config
# RUN mkdir /static
# #ADD Pipfile /config/Pipfile
# #ADD Pipfile.lock /config/Pipfile.lock
# WORKDIR /config

# #RUN apk add --no-cache build-base jpeg-dev zlib-dev
# RUN pip install -U pip
# RUN pip install gunicorn
# #RUN pipenv install --system


# ADD * ${APP_ROOT}

# #RUN mkdir -p  ${LOG_FILE_DIR}
# #RUN touch ${LOG_FILE_PATH}

# WORKDIR ${APP_ROOT}


# ENTRYPOINT gunicorn dcp_site.wsgi --bind=0.0.0.0:8000
# ADD docker-entrypoint.sh ${APP_ROOT}
# RUN chmod 755 docker-entrypoint.sh
# ENTRYPOINT ["docker-entrypoint.sh"]
