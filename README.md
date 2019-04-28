### A simple Flask web app that can be used to accept a healthcheck to make an instance "healthy"
Sometimes you just want to test the creation and the function of the infrastructure, so you need an 'application' to report healthy to the load balancer healthcheck.  But you don't always have a full prod-like environment to run these tests in, including a database or any webservices that the app you're working with is dependent on.

This is just a basic web app that will respond to the kinds of simple healthchecks that an ELB or ALB will send.

## Usage

### install git
yum install git -y

### clone this repo somehwhere on your instance:
git clone https://github.com/BEricDavis/dummy_healthcheck.git && cd dummy_healthcheck

### chmod app.py
chmod 700 app.py

### pip install the requirements
pip install -r requirements.txt

### stop the tomcat app if it's still running
service tomcat8 stop

### start the app.  By default it will listen or port 8080 for requests to '/healthcheck'
app.py

### start the server on port 909 with the default path
app.py --port 9090

### start the server on port 9090 with a custom healthcheck path
app.py --port 9090 --path /myCustomService/healthcheck/health.html

