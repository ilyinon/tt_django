#!/bin/bash
tt_user="admin"
tt_password="admin"
tt_server="10.0.0.20"
tt_port="8000"
my_hostname=`hostname -f`

curl -X POST -i -H "Accept: application/json"  -u ${tt_user}:${tt_password} -d '{"ServerFQDN":"'+${my_hostname}+'"}'  http://${tt_server}:${tt_port}/status/ >> /var/log/heartbeat.log
