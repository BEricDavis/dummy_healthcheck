# A simple Flask web app that can be used to accept an ELB healthcheck to make an instance "healthy"
<p>
## Usage

### clone this repo somehwhere on your instance:
git clone https://github.com/BEricDavis/dummy_healthcheck.git

### pip install the requirements
pip install -r requirements.txt

### stop the tomcat app if it's still running<br>
service tomcat8 stop <br>

### start the server on port 8080 with the default healthcheck path of '/healthcheck'<br>
app.py --port 8080<br>

### start the server on port 8080 with a custom healthcheck path<br>
app.py --port 8080 --path /myCustomService/healthcheck/health.html<br>

