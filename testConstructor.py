import requests
import consul

c =consul.Consul()
def clear_consul(keys):
    """clear counsul keys"""
    try :
        for x in keys:
            c.kv.delete(x)
        result = "ok"
    except:
        result = "failed"
    return result

def posTest(service="web1", url="hello", text="test", keys=["A-GOT", "B-GOT"]):
    """
    Get responce, code, massive of keys and values for request with text parameter
    :param service:
    :param url:
    :param text:
    :param keys:
    :return:
    """
    serveceUrl = "http://" + c.agent.services()[service]['Address'] + ":" + str(c.agent.services()[service]['Port']) + "/" + url
    reqBody = {'text' : text}
    r1=requests.post(url=serveceUrl, json=reqBody)
    keyVal =list(map(lambda x: {x: c.kv.get(x)[1]['Value'].decode("utf-8") }, keys))
    return {"respCode": r1.status_code, "respText" : r1.text, "ConsulKeyVal": keyVal}

def negTest(service="web1", url="hello", text=100):
    """
    Get responce and code for request with bad text parameter
    :param service:
    :param url:
    :param text:
    :param keys:
    :return:
    """
    serveceUrl = "http://" + c.agent.services()[service]['Address'] + ":" + str(c.agent.services()[service]['Port']) + "/" + url
    reqBody = {'text' : text}
    r1=requests.post(url=serveceUrl, json=reqBody)
    return {"respCode": r1.status_code, "respText" : r1.text}

def errorTest(service="web1", url="hello", text=100):
    """
    Get responce and code for request with bad text parameter
    :param service:
    :param url:
    :param text:
    :param keys:
    :return:
    """
    serveceUrl = "http://" + c.agent.services()[service]['Address'] + ":" + str(c.agent.services()[service]['Port']) + "/" + url
    reqBody = {'rext' : text}
    r1=requests.post(url=serveceUrl, json=reqBody)
    return {"respCode": r1.status_code, "respText" : r1.text}
