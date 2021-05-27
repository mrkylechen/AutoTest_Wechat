import pytest
import requests
import time
class TestSignCard:
    @classmethod
    def setup_class(cls):
        cls.access_token = {
            "access_token":"x2IH2_m1UGh5OD580MuO0-ngpam3nwYoVmY0b-tLzQe9pDQrTcdkqZgw--9Ss3HRTWrlcweWZbVxCXJBTb0y0r3plVzB3Y6epFdKSx1JWG8M6MATL-fi5gKsjynHp4Ke3h8mD9xfrTcMoroTc_kVOGgjYkOkmjBpd82KCfMgn_-eOKYuZy3WxYRztcCXXsgABih96N-XtbRxMviqM7Ug4g"
        }
        now = time.time()
        g_now = time.localtime(now)
        cls.datatime = int(now - g_now.tm_hour*60*60 - g_now.tm_min*60 -g_now.tm_sec)
        cls.starttime = cls.datatime
        cls.endtime = int(cls.starttime + 23*60*60 + 59*60 + 59)

    def NOtest_time(self):
        now = time.time()
        g_now = time.localtime(now)
        datatime = now - g_now.tm_hour*60*60 - g_now.tm_min*60 -g_now.tm_sec
        print(datatime)


    def test_option(self):
        self.body = {
            "datetime": self.datatime,
            "useridlist": ["ChenKai"]
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckinoption",params=self.access_token,json=self.body)
        print(r.json())
        global groupid
        groupid = r.json()["info"][0]["group"]["groupid"]
        print(r.json()["info"][0]["group"]["schedulelist"])

    def test_data(self):
        self.body = {
            "opencheckindatatype": 3,
            "starttime": self.starttime,
            "endtime": self.endtime,
            "useridlist": ["ChenKai"]
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckindata",params=self.access_token,json=self.body)
        print(r.json())

    def test_schedulist(self):
        self.body = {
            "groupid": groupid,
            "items": [
                {
                    "userid": "ChenKai",
                    "day": 26,
                    "schedule_id": 0
                }
            ],
            "yearmonth": 202105
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/checkin/setcheckinschedulist",params=self.access_token,json=self.body)
        print(r.json())