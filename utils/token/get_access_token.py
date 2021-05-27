import pytest
import requests
class TestGetToken:
    @classmethod
    def setup_class(cls):
        data_test = {'corpid':'wwbb125cd7f54cba30','corpsecret':'6iOMF9-tJQb3JEcZTboOIJnDGvyw9nzttUlR0iedHKs'}
        cls.r = requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=data_test)
    def test_case1(self):
        print(self.r.json()['access_token'])