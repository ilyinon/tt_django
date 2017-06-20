FROM ubuntu

MAINTAINER TT

RUN export http_proxy=http://192.168.200.4:8080 && export https_proxy=http://192.168.200.4:8080 && apt-get update && apt-get install -y python-pip python-dev
EXPOSE 8000
CMD ["gunicorn", "-w 3", "--bind=0.0.0.0:8000", "project.wsgi"]

ARG base_dir="/u02/tt_django"
WORKDIR ${base_dir}

COPY ./requirements.txt ${base_dir}/requirements.txt
RUN export http_proxy=http://192.168.200.4:8080 && export https_proxy=http://192.168.200.4:8080 && pip install -r ${base_dir}/requirements.txt

COPY . ${base_dir}

 
