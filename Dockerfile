FROM python:latest

ENV DockerHOME=/home/app/webapp
ENV NODE_MANAGER_URL='http://10.7.0.1:8888/config'
Env LOC_NETWORK='10.7.0.0/16'

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

COPY . $DockerHOME

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

EXPOSE 8000

CMD python ./notifyweb/manage.py runserver 0.0.0.0:8000
