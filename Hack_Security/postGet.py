import requests

def post(url, data=None, json=None, **kwargs):
    return requests.post(url,data,json,**kwargs)

def Get(url, params=None, **kwargs):
    return requests.get(url,params,**kwargs)



