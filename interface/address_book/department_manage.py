import os,sys
sys.path.append(os.getcwd())

import time
import requests
from utils.requests.request_class import RequestClass
class DepartmentManage:
    # def __init__(self):
    #     token_request = {'corpid': 'wwbb125cd7f54cba30', 'corpsecret': '6iOMF9-tJQb3JEcZTboOIJnDGvyw9nzttUlR0iedHKs'}
    #     r = requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=token_request)
    #     self.access_token = r.json()['access_token']
    def __init__(self):
        self.request = RequestClass()

    def get_token(self):
        token_request = {'corpid': 'wwbb125cd7f54cba30', 'corpsecret': '6iOMF9-tJQb3JEcZTboOIJnDGvyw9nzttUlR0iedHKs'}
        r = requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=token_request)
        self.access_token = r.json()['access_token']
        return r

    def get_deplist(self,dep_id):
        self.params = {
            'access_token':self.access_token,
            'id':dep_id
        }
        r = self.request.request_get(url="https://qyapi.weixin.qq.com/cgi-bin/department/list",params=self.params)
        return r

    def add_dep(self,name,parentid):
        self.params = {
            'access_token':self.access_token
        }
        self.body = {
            'name': name,
            'parentid': parentid
        }
        r = self.request.request_post(url="https://qyapi.weixin.qq.com/cgi-bin/department/create",params=self.params,body=self.body)
        return r

    def update_dep(self,id,name):
        self.params = {
            'access_token': self.access_token
        }
        self.body = {
            'id': id,
            'name': name
        }
        r = self.request.request_post(url="https://qyapi.weixin.qq.com/cgi-bin/department/update",params=self.params,body=self.body)
        return r

    def delete_dep(self,id):
        self.params = {
            'access_token': self.access_token,
            'id':id
        }
        r = self.request.request_get(url="https://qyapi.weixin.qq.com/cgi-bin/department/delete", params=self.params)
        return r
