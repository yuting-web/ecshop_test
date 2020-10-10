# @Time : 2020/10/10 15:41
# @Author : 30037
# @Email : scg@gmail.com
# @File : config.py
# @Project : test_ecshop

import os

LOGIN_URL = "http://192.168.1.164/upload/admin"
#工程的绝对路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__)).split('conf')[0]
#用例的绝对路径
CASE_PATH = os.path.join(BASE_PATH,"testcase")
#报告的绝对路径
REPORT_PATH = os.path.join(BASE_PATH,'report')



