#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
封装邮件服务模块
测试报告作为附件发送到对应邮箱
"""

import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def send_main(file_path, mail_to='guliangce@163.com'):
    mail_from = 'guliangce@163.com'
    f = open(file_path, 'rb')
    mail_body = f.read()
    f.close()

    # msg = email.MIMEMultipart.MIMEMultipart()
    msg = MIMEMultipart()

    # 构造MIMEBase对象做为文件附件内容并附加到根容器
    contype = 'application/octet-stream'
    maintype, subtype = contype.split('/', 1)

    # 读入文件内容并格式化
    data = open(file_path, 'rb')
    file_msg = MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()

    encoders.encode_base64(file_msg)

    # 设置附件头
    basename = os.path.basename(file_path)
    file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
    msg.attach(file_msg)
    print(u'msg 附件添加成功')

    msg1 = MIMEText(mail_body, "html", 'utf-8')
    msg.attach(msg1)

    if isinstance(mail_to, str):
        msg['To'] = mail_to
    else:
        msg['To'] = ','.join(mail_to)
    msg['From'] = mail_from
    msg['Subject'] = u'Liunx_GUI自动化回归测试'
    msg['date'] = time.strftime('%Y-%m-%d-%H_%M_%S')
    print(msg['date'])

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('guliangce@163.com', 'cytest3611653a')  # 登录账号和密码（密码为之前申请的授权码）
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print('email has send out !')
