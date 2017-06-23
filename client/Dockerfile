FROM ubuntu

MAINTAINER TT

#RUN export http_proxy=http://192.168.200.4:8080 && \
#     export https_proxy=http://192.168.200.4:8080 && \
#     apt-get update && apt-get -y install cron curl && \
#     chmod +x /bin/check_client.sh && echo "* * * * * root /bin/check_client.sh" >> /etc/crontab
RUN apt-get update && apt-get -y install cron curl && \
    chmod +x /bin/check_client.sh && echo "* * * * * root /bin/check_client.sh" >> /etc/crontab

COPY ./check_client.sh /bin/check_client.sh
ENTRYPOINT cron -f
