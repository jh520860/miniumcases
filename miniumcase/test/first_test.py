#!/usr/bin/env python3
import random
import time
from itertools import combinations
import threading
from miniumcase.logs.log import MyLogger
import minium
from  miniumcase.base.basepage import BasePage
from minium import Callback

log = MyLogger()


class FirstTest(minium.MiniTest):



    def __init__(self, methodName='runTest'):
        super(FirstTest, self).__init__(methodName)
        self.base = BasePage(self)



    def test_01(self):
        called = threading.Semaphore(0)
        #callback = Callback()  # 监听回调, 阻塞当前主线程
        callback_args = None
        def callback(args):
            nonlocal callback_args
            called.release()
            callback_args = args
        self.page.wait_for(2)
        # self.app.redirect_to("/pages/assess/sign")
        # element = self.page.get_element("canvas")
        # element.move(30, 70, 500)
        # self.base.element_tap_class()


        self.base.elements_tap_class(0,'btn_text','练习模式') #进入练习模式
        self.page.wait_for(2)				# 当前页面等待2s


        self.page.get_elements("van-radio-group")[0].get_elements("van-radio")[1].get_element("view").get_element("van-icon").get_element("view").tap()

        for lennums in range(0,5) :
            self.page.wait_for(1)
            inputnum = self.base.element_input_num()
            radionum= self.base.element_radio_num()
            checknum= self.base.element_checkbox_num()


            if inputnum != 0 :
                if lennums != 4    :
                    for i in range (0,inputnum) :
                        self.base.shadow_input_text(i,'123456789','输入框')

                else:
                    if inputnum != 1 :
                        for i in range(0, inputnum-1):
                            self.base.shadow_input_text(i, '123456789', '输入框')
                    else:
                        self.base.shadow_input_textarea(0,'123456789','输入框')


            if radionum != 0 :

                for i in range (0,radionum) :
                    radionums= self.base.element_radio_nums(i)

                    randomnum = random.randint(0,radionums -1 )

                    self.base.element_tap_radio(i,randomnum)

            if checknum != 0 :

                for i in range (0,checknum) :

                    checknums= self.base.element_checkbox_nums(i)
                    randomnum = random.randint(0,checknums -1)
                    for j in range (0,randomnum) :
                        randomnum = random.randint(0,checknums -1)
                        self.base.element_tap_checkbox(i,randomnum)


            if lennums ==3  :
                self.base.elements_tap_class(1,'nextBtn','下一步')
            else:
                self.base.elements_tap_class(0,'nextBtn','下一步')




        self.base.element_tap_class('nextBtn','开始评估') #进入评估做题

        # self.base.elementtext_is_exists('上传评估结果')
        # self.base.elementtext_is_exists('中华人民共和国民政部老年人能力评估')



        for k in range (0,4) :
            self.page.wait_for(2)
            #log.info(k)
            #zjname = self.base.elements_shaow_text(k,'章节名字')
            self.base.elements_tap_class(k,'item_title','第'+str(k+1)+ '章节') #进入详细题目
            self.page.wait_for(2)
            l = 0
            if k == 0 :
                l=8
            elif k ==1 :
                l=4
            elif k == 2 :
                l = 9
            elif k == 3:
                l = 5

            for j in range(0,l) :
                self.page.wait_for(2)
                radionum= self.base.element_radio_num()
                for i in range (0,radionum) :
                    n = random.randint(0,1)
                    self.base.element_tap_radio(i,n)

                strss=self.base.elements_text(0,'nextBtn','完成')
                num1=strss[0:1]
                num2=strss[2:3]
                if (num1 == num2) :
                    self.base.elements_tap_class(0,'nextBtn','完成')
                    self.page.wait_for(2)
                    if j == l-1 :
                        self.base.elements_tap_class(2,'nextBtn','返回，下一章')
                    else:
                        if (self.base.elements_text(1,'nextBtn','返回，下一章') == '返回，下一章') :
                            self.base.elements_tap_class(1,'nextBtn','返回，下一章')
                            break
                        else :
                            self.base.elements_tap_class(1,'nextBtn','下一节')
                else:
                    i = i-1


        self.page.wait_for(2)
        self.base.element_tap_image('aspectFill', '上传结果')

        self.page.wait_for(2)
        self.base.element_is_exists('评估得分')
        self.base.element_is_exists('评估结果')
        self.base.element_is_exists('是否变更等级')
        self.base.element_is_exists('提交')

        self.base.elements_tap_class(0,'nextBtn','提交')

        self.base.element_is_exists('评估签名')

        self.base.elements_tap_class(1,'nextBtn','评估签名')

        self.page.wait_for(2)

        self.base.element_is_exists('提交')

        self.base.element_tap_button(0,'评估员签名')
        self.page.wait_for(2)
        self.base.element_is_exists('提交')
        self.base.element_is_exists('清除')

        element = self.page.get_element("canvas")
        element.move(30, 70, 500)
        self.base.element_view_tap('提交')
        self.page.wait_for(2)
        self.base.element_view_tap('信息提供人签名')
        self.page.wait_for(2)
        self.base.element_is_exists('提交')
        self.base.element_is_exists('清除')

        element = self.page.get_element("canvas")
        element.move(30, 70, 500)
        self.base.element_view_tap('提交')

        self.page.wait_for(2)
        self.base.element_view_tap('提交')
        self.page.wait_for(2)

        self.base.element_is_exists('非常满意')
        self.base.element_is_exists('满意')
        self.base.element_is_exists('一般')
        self.base.element_is_exists('不满意')
        self.base.element_is_exists('非常不满意')
        self.base.element_is_exists('完成')
        self.base.element_is_exists('删除')

        self.base.element_view_tap('非常满意')

        self.app.hook_wx_method("showModal", callback=callback)
        self.base.element_view_tap('删除')
        time.sleep(1)
        self.native.handle_modal("删除")


        self.page.wait_for(2)










    @minium.skip("跳过该用例")
    def test_02(self):

        #self.app.redirect_to("/pages/account/mode")

        self.page.wait_for(2)
        self.base.element_is_exists('老年人能力评估')
        self.base.element_is_exists('练习模式')
        self.base.element_is_exists('实训考试')
        self.base.element_is_exists('理论考试')
        self.base.elements_tap_class(1,'btn_text','实训考试') #进入考试模式
        self.page.wait_for(1) #等待1s
        self.base.element_is_exists('考试记录')
        self.base.element_tap_class('list_item','继续考试')  #进入人员编辑页面
        self.page.wait_for(1) #等待1s
        self.base.element_is_exists('评价信息')
        self.base.element_is_exists('评估编号')
        self.base.element_is_exists('评估基准日期')
        self.base.element_is_exists('评估原因')
        self.base.element_is_exists('首次评估')
        self.base.element_is_exists('常规评估')
        self.base.element_is_exists('即时评估')
        self.base.element_is_exists('因评估结果有疑问进行的复评')
        self.base.element_is_exists('其它')

        self.page.wait_for(2) #等待
        self.base.shadow_input_text(0,'2023071815475')
        self.base.shadow_input_text(1,'2023-07-18')
        self.page.wait_for(1) #等待
        #self.base.element_tap_shaow(0,1,"常规评估")


        self.page.wait_for(2)				# 当前页面等待2s

    @minium.skip("跳过该用例")
    def test_03(self):
        called = threading.Semaphore(0)
        #callback = Callback()  # 监听回调, 阻塞当前主线程
        callback_args = None
        def callback(args):
            nonlocal callback_args
            called.release()
            callback_args = args
        #self.app.redirect_to("/pages/account/mode")
        self.base.elements_tap_class(2,'btn_text','理论考试') #进入理论考试
        self.page.wait_for(1) #等待1s
        self.base.element_is_exists('考试记录')

        self.page.get_element("image[mode='aspectFit']").tap() #进入考试页面
        self.page.wait_for(1) #等待1s
        if (self.base.element_is_exists('考试') == True) :
            self.native.handle_modal("确定")
            is_called = called.acquire(timeout=10)
        # # 释放hook showModal方法
        # self.app.release_hook_wx_method("showModal")
        # self.assertTrue(is_called, "callback called")
        # self.assertDictContainsSubset( {"errMsg": "showModal:ok", "cancel": False, "confirm": True}, callback_args[0])



        self.page.wait_for(2) #等待1s
        self.base.element_is_exists('当前考试完成：')
        self.base.element_is_exists('完成交卷')
        self.base.element_is_exists('结束时间')

        # 点击25个选项
        checknum= self.base.element_checkbox_num()
        #log.info("多选一共有: " + str(checknum))
        radionum= self.base.element_radio_num()
        #log.info("单选一共有: " + str(radionum))

        for i in range(0,radionum) : #做单选题

            #self.page.wait_for(1) #等待1s
            n = random.randint(0,3)
            self.base.element_tap_radio(i,n)


        for j in range(0,checknum) : #做多选题

            #self.page.wait_for(1) #等待1s

            for k in range (0,5) :

                #self.page.wait_for(1) #等待1s
                n = random.randint(0,4)
                self.base.element_tap_checkbox(j,n)



        self.page.wait_for(1) #等待1s

        if (self.base.element_is_exists('25/25') == True) :
            self.app.hook_wx_method("showModal", callback=callback)
            self.base.element_tap_class('nextBtn','完成交卷')
            time.sleep(2)
            self.native.handle_modal("确定")
            is_called = called.acquire(timeout=10)
            # 释放hook showModal方法
            # self.app.release_hook_wx_method("showModal")
            # self.assertTrue(is_called, "callback called")
            # self.assertDictContainsSubset( {"errMsg": "showModal:ok", "cancel": False, "confirm": True}, callback_args[0])

            time.sleep(2)
            self.native.handle_modal("确定")
            is_called = called.acquire(timeout=10)
            # 释放hook showModal方法
            #self.app.release_hook_wx_method("showModal")
            # self.assertTrue(is_called, "callback called")
            # self.assertDictContainsSubset( {"errMsg": "showModal:ok", "cancel": False, "confirm": True}, callback_args[0])



















if __name__ == "__main__":

    import unittest
    loaded_suite = unittest.TestLoader().loadTestsFromTestCase(FirstTest)
    result = unittest.TextTestRunner().run(loaded_suite)