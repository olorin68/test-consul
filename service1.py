from flask import Flask, jsonify
from flask import make_response
from flask import request
import json
import consul
import requests

c =consul.Consul()
service = Flask(__name__)


@service.route('/hello', methods=['POST'])
def hello_text():
    try:
        val = json.loads(request.data)['text']
        print(val)
        if val !=None and type(val) == str:
            c.kv.put("A-GOT", val.encode('utf-8'))
            resp = {"text":"get your text", "code": 200}
        else:
            resp = {"text":"Some problem with your text, please fill it by string", "code": 400}
    except:
        resp = {"text": "something went wrong", "code": 500}
    try:
        reqBody={"text": resp["text"]+ " with "+ str(resp["code"])+ " status code"}
        serveceUrl= "http://"+ c.agent.services()['web2']['Address']+ ":"+ str(c.agent.services()['web2']['Port']) +"/other"
        requests.post(url=serveceUrl, json=reqBody)
    except:
        resp = {"text": "something went wrong", "code": 504}
    return make_response(resp["text"]),resp["code"]



if __name__ == '__main__':
    service.run(debug=True, host='127.0.0.1', port=8081)
