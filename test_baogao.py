import unittest

#创建套件
suite1 = unittest.TestLoader().discover(r"E:\python_html",pattern='test_y*.py')


#将该套件的测试结果集成到测试报告中

#例一：


# from calsses_28.HTMLTestRunner import HTMLTestRunner   #导入包
#
# report_path = 'test_report.html'    #(这里定义的html文件即为测试报告的名字，也可以不定义，直接在open里写入以html结尾的文件，文件不存在会新建，如例二)
# with open (report_path,'wb') as f: #以二进制写的方式打开此测试报告，形成文件操作对象f
#     runner = HTMLTestRunner(f,title='测试报告',description='v1.0')  #利用HTMLTestRunner生成运行器runner,注意HTMLTestRunner
# #后的三个参数，第一个为stream:文件操作的对象；二为title：此为测试报告的标题；三为descrption:测试报告中对此次测试报告的描述）
#     runner.run(suite1) #通过运行器运行测试套件
#

#例二

from HTMLTestRunner import HTMLTestRunner


with open('test1_report.html','wb',) as f:
    runner = HTMLTestRunner(stream=f,title='登录模块测试报告',description='v1.2')
    runner.run(suite1)