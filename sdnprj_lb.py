from flask import Flask
import os
import requests

app = Flask(__name__)


lb_scheme=os.getenv('LB')
# print(lb_scheme)

server1='20.238.49.249'
server2='52.138.220.51'

if lb_scheme=='rr':
    rr_value=0
    @app.route('/')
    def round_robin():
        global rr_value
        if rr_value==0:
            response = requests.get(f'http://{server1}:8080').text
            rr_value=1
            return response
        elif rr_value==1:
            response=requests.get(f'http://{server2}:8080').text
            rr_value=0
            return response

elif lb_scheme=='wrr':
    weights=[5,3]
    count_s1=0
    count_s2=0
    server=0
    @app.route('/')

    def wrr():
        global count_s1,count_s2,server
        if server==0:
            if count_s1<weights[0]:
                count_s1+=1
                response = requests.get(f'http://{server1}:8080').text
                return response
            else:
                server=1
                count_s2+=1
                count_s1=0
                response = requests.get(f'http://{server2}:8080').text
                return response
        elif server==1:
            if count_s2<weights[1]:
                count_s2+=1
                response = requests.get(f'http://{server2}:8080').text
                return response
            else:
                server=0
                count_s1+=1
                count_s2=0
                response = requests.get(f'http://{server1}:8080').text
                return response

elif lb_scheme=='load':
    @app.route('/')
    def load_sense():
        load1=float(requests.get(f'http://{server1}:8080/cpu').text)
        load2=float(requests.get(f'http://{server2}:8080/cpu').text)
        if load1<load2:
            response = requests.get(f'http://{server1}:8080').text
            return response
        else:
            response = requests.get(f'http://{server2}:8080').text
            return response
    @app.route('/load')
    def show_load():
        load1=float(requests.get(f'http://{server1}:8080/cpu').text)
        load2=float(requests.get(f'http://{server2}:8080/cpu').text)
        return f'load os server1 = {load1}, load of server2 = {load2}'


# print("load of server 1 is ", requests.get(f'http://{server1}:8080/cpu').text ) 
# print("load of server 2 is ", requests.get(f'http://{server2}:8080/cpu').text) 


if __name__=="__main__":
    app.run(host='0.0.0.0', port=4000)

