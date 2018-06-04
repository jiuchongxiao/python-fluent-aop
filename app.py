from aop.aspectAop import InvocationLoggerAspect
from flask import Flask, request
import requests
import os
import socket


import urllib3

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

from fluent import sender, event

# Connect to Redis
# redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)

# from flask_bootstrap import Bootstrap
# Bootstrap(app)


sender.setup('helloworld', host='192.168.181.99', port=30224)
# sender.setup('helloworld', host='fluentd-es.logging', port=24224)
@app.route("/")
@InvocationLoggerAspect
def hello():
    event.Event('follow-event-base', {
        'from': 'userA',
        'to':   'userB'
    })
    visits = "hahahahahhahahahahahhahahahahhaahhaha..."
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> ${visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)
	
@app.route('/python-sa-noheader/info')
@InvocationLoggerAspect
def portalRouteNoheader():
    url = "http://192.168.181.99:32693/sa/info"
    # url = "http://service-a:8081/sa/info"
    req = urllib3.PoolManager()
    res_data = req.request('Get',url)
    event.Event('portalRouteNoheader', {
        'status': res_data.status,
        'data':   res_data.data
    })
    print(res_data.status)
    return res_data.data



@app.route("/login",methods = ['POST','GET'])
@InvocationLoggerAspect
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        return "post"
    if request.method == "GET":
        print('call get now')

        username = request.args.get('username')
        password = request.args.get('password')
        print (username)
        print (password)
        return  "get"

@app.route('/python-sa/info')
@InvocationLoggerAspect
def portalRoute():
    headers = getForwardHeaders(request)
    portal = getProductReviews(headers)
    event.Event('portalRoute', {
        'data': portal
    })
    return portal


@InvocationLoggerAspect
def getProductReviews(headers):
    ## Do not remove. Bug introduced explicitly for illustration in fault injection task
    ## TODO: Figure out how to achieve the same effect using Envoy retries/timeouts
    url = "http://192.168.181.99:32693/sa/info"
    # url = "http://service-a:8081/sa/info"
    res = requests.get(url, headers=headers, timeout=10.0)
    return res.text
    
	
	

def getForwardHeaders(request):
    headers = {}

    user_cookie = request.cookies.get("user")
    if user_cookie:
        headers['Cookie'] = 'user=' + user_cookie

    incoming_headers = [ 'x-request-id',
                         'x-b3-traceid',
                         'x-b3-spanid',
                         'x-b3-parentspanid',
                         'x-b3-sampled',
                         'x-b3-flags',
                         'x-ot-span-context'
    ]

    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val
            #print "incoming: "+ihdr+":"+val

    return headers
	

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8090)

