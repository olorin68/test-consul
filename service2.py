from flask import Flask, jsonify
from flask import make_response
from flask import request
import json
import consul

c =consul.Consul()
service = Flask(__name__)


@service.route('/other', methods=['POST'])
def hello_text():
    try:
        val = json.loads(request.data)['text']
        c.kv.put("B-GOT", val)
        return make_response("all right")
    except:
        return make_response("somethung went wrong"), 500

if __name__ == '__main__':
    service.run(debug=True, host='127.0.0.1', port=8082)
