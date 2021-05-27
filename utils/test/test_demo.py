import pytest
import requests
class TestWechat:
    @classmethod
    def setup_class(cls):
        cls.data_params = {'access_token':'kx2d9fHFBjdQk5E35993sZp95Hg500aw1JZ8q02oT3yxRQXtEfEiV38tNjj-ZSCL9mIrRtAK6N7nWX_MwTB4hLfPApYJZyhWvw-KRptREpHsp8gD_z0FxHHAbSJfAAP8zAQRYcc23kFSgOq3JUwwIMQgjS0IKH85tpt8aKLcm0HjsHEJsh_gl3-cJ5_uN57e3h67W82v3D3aMm1YlrzfaQ'}
        # data_body = {
        #     "touser": "@all",
        #     "msgtype": "text",
        #     "agentid": 1000003,
        #     "text": {
        #         "content": "你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"
        #     },
        #     "safe": 0,
        #     "enable_id_trans": 0,
        #     "enable_duplicate_check": 0,
        #     "duplicate_check_interval": 1800
        # }
        # print(data_params['access_token'])
        # print(type(data_params['access_token']))
        # cls.r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token_value}".format(token_value=data_params['access_token']),json=data_body)
        # cls.r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send",params=cls.data_params,json=data_body)
    def notest_creat_dep(self):
        print("pass")

    def notest_case1(self):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/list", params=self.data_params)
        global dep_id
        dep_id = r.json()["department"][0]["id"]
        print(format(r.json()))
        print(dep_id)

    def notest_case2(self):
        self.params = {
            'access_token': 'kx2d9fHFBjdQk5E35993sZp95Hg500aw1JZ8q02oT3yxRQXtEfEiV38tNjj-ZSCL9mIrRtAK6N7nWX_MwTB4hLfPApYJZyhWvw-KRptREpHsp8gD_z0FxHHAbSJfAAP8zAQRYcc23kFSgOq3JUwwIMQgjS0IKH85tpt8aKLcm0HjsHEJsh_gl3-cJ5_uN57e3h67W82v3D3aMm1YlrzfaQ',
            'department_id':dep_id,
            'fetch_child':1
        }
        # self.r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list", params=self.data_params)
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",params=self.params)
        print(r.text)
        # print("end")