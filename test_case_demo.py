#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
这是一个测试用例模板

测试用例:测试文档编辑器LibreOffice,创建word文档，输入文字并能正常保存。

执行步骤：
1.打开文档编辑器 LibreOffice。
2.新建一个word文件。
3.输入 www.baidu.com。
4.保存文件。
5.关闭LibreOffice。

预期结果:
1.可以正常打开LibreOfficed,打开的是 LibreOffice 创建文档的首页。（通过图片对比）
2.word编辑器被打开。
3.能够正常输入。(通过图片对比)
4.保存成功。（检查保存目录下是否有存档文件。）
5.关闭成功。

'''

#加载系统模块
import logging
#加载unittest
import unittest
#加载图形对比模块
import img_contrast as ic
#加载pywinauto
from pywinauto.application import Application
from pywinauto import mouse

APP_PATH = 'D:\\guiqtdemochip\\chip.exe'
IMG_PATH0 = 'C:\\Users\\gulia\\PycharmProjects\\GuiAuto\\IMG\\demo_img0.png'
IMG_PATH1 = 'C:\\Users\\gulia\\PycharmProjects\\GuiAuto\\IMG\\demo_img1.png'

#测试用例类
class TestCaseDemo(unittest.TestCase):
    """测试用例 demo"""

    # 初始化函数
    def step_init(self):
        logging.info('启动应用'+APP_PATH)
        #通过路径启动应用
        self.app = Application('uia').start(APP_PATH)
        self.dlg = self.app['Chip Example']
        logging.info('最大化')
        self.dlg.maximize()
        logging.info(self.dlg)

    # 通过按钮名称点击窗口控件
    def step_select_button(self):
        #获取最左边的Drag按钮，并点击
        top_left_view = self.dlg['Top left viewCustom']
        top_left_view.child_window(title="Drag", control_type="CheckBox").click()
        #获取最左边的Drag按钮，并点击
        top_left_view.child_window(title="Select", control_type="CheckBox").click()

    #放大画布
    def step_scroll_bar(self):
        # 点击10次放大按钮
        slider = self.dlg['Pointer ModeSlider1']
        slider.press_mouse_input(coords=(1227,408))
        slider.release_mouse_input(coords=(1231,329))
        logging.info(slider.legacy_properties().get('Value'))

    #拖动芯片
    def setp_move_chip(self):
        # 移动其中一个芯片的位置
        mouse.press(coords=(454,393))
        mouse.release(coords=(978,276))

    #截屏
    def step_screen_shot(self):
        canvas = self.dlg["Top left viewCustom2"]
        logging.info('截屏！')
        canvas.capture_as_image().save(IMG_PATH1)

    def step_assert(self):
        ima0 = ic.getImageFile(IMG_PATH0)
        ima1 = ic.getImageFile(IMG_PATH1)
        self.assertTrue(ic.CompareImage(ima0, ima1))

    # 测试步骤的执行
    def test_go(self):
        logging.info('运行用例！')
        self.step_init()
        self.step_select_button()
        self.step_scroll_bar()
        self.setp_move_chip()
        self.step_screen_shot()
        self.step_assert()

    def tearDown(self):
        self.app.kill(soft=True)
        logging.info('测试已完成')