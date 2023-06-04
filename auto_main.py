#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
这是gui自动化的主程序
"""
# 加载unittest模块
import unittest
# 加载日志模块
import logging
from auto_log import *
# 加载报告模块
from BeautifulReport import BeautifulReport as bf
# 加载邮件模块
from mail import *

# 定义全局变量
# 日志保存目录
LOG_DIR = "C:\\Users\\gulia\\PycharmProjects\\GuiAuto\\logs"
# 测试名称（日志用）
TEST_NAME = 'auto_gui_test'
# 报告名称
REPORT_NAME = "C:\\Users\\gulia\\PycharmProjects\\GuiAuto\\testreport"
# 报告发送地址
MAIL_ADD = 'guliangce@163.com'

if __name__ == '__main__':
    write_log(LOG_DIR, TEST_NAME)
    log = logging.getLogger()
    # 设置报告名称
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    report_name = now + '-' + 'demo_liunx_autotest_gui' + '_test_report.html'
    # 加载测试用例文件
    discover = unittest.defaultTestLoader.discover("C:\\Users\\gulia\\PycharmProjects\\GuiAuto", pattern='test*.py')
    # 启动测试++
    try:
        log.info("运行自动化！")
        run = bf(discover)
        run.report(filename=report_name, report_dir=REPORT_NAME, description='本轮测试结果如下')
        send_main(file_path=REPORT_NAME + report_name, mail_to=MAIL_ADD)
        log.info("send mail!!!")
    except Exception as e:
        log.error(repr(e))
        log.error("自动化测试运行出错！检查日志！")