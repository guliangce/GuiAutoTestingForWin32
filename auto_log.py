#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
这是gui自动化的日志模块
"""

#加载日志模块
import logging
#加载时间模块
import time

#定义写日志函数

def write_log(log_dir, name_project):
    print('写日志.......................')
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename= log_dir + name_project + now+'.log',
                        filemode='w')
    logging.info(now +  name_project + '.log')
