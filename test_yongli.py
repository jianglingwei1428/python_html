import unittest
from login_hanshu import login

class TestLogin(unittest.TestCase):

    # case1 ：验证正确的用户名和密码进行登录
    @unittest.skip('该条用例不执行')
    def testlogin1(self):
        self.assertEqual('登录成功',login('admin','123456'))

    # case2 : 验证正确的用户名和空的密码
    def testlogin2(self):
        self.assertEqual('用户名不能为空',login(' ','123456'))

    # case3 :验证密码不能为空
    def testlogin3(self):
        self.assertEqual('密码不能为空',login('admin',' '))