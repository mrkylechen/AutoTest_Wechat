import os, sys
path = os.path.abspath(__file__)
for i in range(3):
  path = os.path.dirname(path)
  sys.path.append(path)

import pytest
import time
from interface.address_book.department_manage import DepartmentManage

class TestDeparmentMange:
    @classmethod
    def setup_class(cls):
        cls.depmange = DepartmentManage()
        cls.depmange.get_token()

    def test_deplist(self):
        r = self.depmange.get_deplist(1)
        print(r.json())
        assert r.json()['errcode'] == 0

    def test_add_dep(self):
        r = self.depmange.add_dep(name='开发组',parentid=1)
        print(r.json())
        assert r.json()['errcode'] == 0

    def test_update_dep(self):
        r = self.depmange.update_dep(id=1,name='产品中心')
        print(r.json())
        assert r.json()['errcode'] == 0
    def test_delete_dep(self):
        r = self.depmange.delete_dep(id=3)
        print(r.json())
        assert r.json()['errcode'] == 0