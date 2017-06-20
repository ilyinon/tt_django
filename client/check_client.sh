#!/bin/bash
tt_user="admin"
tt_password="admin"
tt_server="10.0.0.20"
tt_port="8000"

curl -X POST  -u ${tt_user}:${tt_password} -d ServerFQDN=`hostname -f`  http://${tt_server}:${tt_port}/status/
