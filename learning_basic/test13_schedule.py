# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test13_schedule.py
# @Time : 2023/8/24 8:14
# @Tool : PyCharm

import schedule
import time


def job():
    print('hahahaha...')

schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
