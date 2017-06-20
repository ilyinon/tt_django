This is example of implementation Django API. There is only one model which include FQDN and Timespamp.
There are available two methods for API interaction: 
  - get statistics
  - send statistic of current server

There are three docker containers:
 - client, which run script for sending statistics to server
 - server, which start Django application for processing request
 - database, postgres, which is using for storing data by server

For deploy all solution just run: 
 ```make deploy-all```




There are presets:
 - user and password for accessing Django application:
    ```admin:admin```
 - IP addresses:
    10.0.0.10 - postgres
    10.0.0.20 - server, Django API
    10.0.0.30 - client


Useful CURL command:

Get statistics

```curl -H 'Accept: application/json; indent=4' -u admin:admin  http://10.0.0.20:8000/status/```

Send statistics:

```curl -X POST -i -H "Accept: application/json"  -u admin:admin -d '{"ServerFQDN":"server1"}'  http://10.0.0.20:8000/status/```
