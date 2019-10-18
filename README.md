# Prometheus Monitoring and alerting
Servers Monitoring with Prometheus

Youtube Video Tutorial: https://www.youtube.com/watch?v=DCv09aOKK1c&t=297s 

Commands:
First of all run prometheus server
Command to run Prometheus
$ ./prometheus --config.file=prometheus.yml

Then run alertmanager
Command to run alertmanager
$ ./alertmanager --config.file=alertmanager.yml

Then run pushgateway on servers
Command to run pshgateway
$ ./pushgateway

Now Run the Script on Server by using following commnad
$ while sleep 1; do ./getCronProcess.sh; done;
This script will scape the metrics of all process running on server and will pass to pushgateway

Alertmanager will pull those metrics from pushgateway

Now open the Server_Webhook.py file in any python editor and run this flask app

Keep in mind a webhook link which we pass to alertmanager.yml file will be derived by ngrok software

So to make our webhook work download the ngrok software from here https://ngrok.com/download 

Go the that dirctory where ngrok is downloaded and run it by using following command

$ ./ngrok http 5003

This will provide a public link, copy that link and past it in alertmanager webhook field
e.g
Forwarding                    http://20c1db33.ngrok.io -> http://localhost:5003 
Forwarding                    https://20c1db33.ngrok.io -> http://localhost:5003

Copy the first link  http://20c1db33.ngrok.io and use it in alertmanager

