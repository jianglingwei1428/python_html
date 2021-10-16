#测试用例的入口，所有的测试用例都从该入口去运行，从这个里面去组装套件，运行套件


import unittest
#1、创建套件
suite = unittest.TestLoader().discover('E:\\untitled\\calsses_28',pattern='ceshi*.py')
#2、创建运行器

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)#运行时被搜索文件的代码不可置灰，置灰不执行
