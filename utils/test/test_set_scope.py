import pytest
import requests
class TestScope:
    @classmethod
    def setup_class(cls):
        cls.data_params = {
            'access_token': 'il1BG61UBgV7lbOUPZAQpqKJu2X6Rlp278bZvmcAMad3PRyTSl9yCueM6jPXhB9d8TBQEBq6MM1JN_exPEZ5-ux1mjlmk-oO2X_yGRbMvRUjKfSWAH2x6CzhrmqrFvDvlPmXseQN2Hk6RyBv8x85SA2jD_Qm6XIRx-1kaGh8uKv932zVrN7jZ2wA95v06r8Uv7p7pFDSjHbfgzQvtpRKcQ'
        }
        cls.body = {
            "agentid":3010011,
            "allow_user": ["陈凯", "BBQ"],
            "allow_party": ["英雄训练营","测试组"],
            "allow_tag": ["一般","重要"]
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/agent/set_scope",params=cls.data_params,json=cls.body)
        print(r.text)

    def test_case1(self):
        print("case1")