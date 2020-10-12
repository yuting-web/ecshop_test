# @Time : 2020/10/13 0:13
# @Author : 30037
# @Email : 960364395@qq.com
# @File : runner.py
# @Project : test_ecshop
import unittest
from conf.config import CASE_PATH,REPORT_PATH
from BeautifulReport import BeautifulReport
import time

#创建测试集
suite = unittest.defaultTestLoader.discover(CASE_PATH,'*_case.py')
#创建执行器
runner = BeautifulReport(suite)
#报告取名
filename = "{}{}.html".format("test_report",time.strftime("%Y%m%d%H%M"))
#执行
runner.report(description="crm测试报告",
              filename=filename,
              report_dir=REPORT_PATH)