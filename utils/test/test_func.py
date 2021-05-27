import pytest
class TestFunc:
    def test_case1(self):
        str1 = "http://www.baidu.com?data={value}"
        str2 = str1.format(value='test')
        print(str1)
        print(str2)