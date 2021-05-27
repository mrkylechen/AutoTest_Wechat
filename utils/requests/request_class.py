import requests
class RequestClass:
    def request_post(self,url,params,body):
        r = requests.post(url=url,params=params,json=body)
        return r
    def request_get(self,url,params):
        r = requests.get(url=url,params=params)
        return r