import  minium
from miniumcase.logs.log import MyLogger
log = MyLogger()
import  os


class BasePage():
    def __init__(self, mini):
        self.mini = mini



    def navigate_to_open(self, route):
        """以导航的方式跳转到指定页面,不允许跳转到 tabbar 页面,支持相对路径和绝对路径, 小程序中页面栈最多十层"""
        self.mini.app.navigate_to(route)

    def redirect_to_open(self, route):
        """关闭当前页面，重定向到应用内的某个页面,不允许跳转到 tabbar 页面"""
        self.mini.app.redirect_to(route)

    def switch_tab_open(self, route):
        """跳转到 tabBar 页面,会关闭其他所有非 tabBar 页面"""
        self.mini.app.switch_tab(route)

    @property
    def current_title(self) -> str:
        """获取当前页面 head title, 具体项目具体分析,以下代码仅用于演示"""
        return self.mini.page.get_element("XXXXXX").inner_text

    def current_path(self) -> str:
        """获取当前页面route"""
        return self.mini.page.path

    def elements_tap_class(self,i, route,name):
        """点击元素"""

        log.info("点击元素: " + name)
        try:
            self.mini.page.get_elements("[class='"+route+"']", max_timeout=3)[i].tap()

        except IOError  as e:
            #self.mini.page.capture("F://桌面/assessment截图/" + route +'jpg')
            log.error('没有找到对应的元素：' + name + ";      报错信息是：" + str(e))



    def element_tap_class(self, route,name):
        """点击元素"""

        log.info("点击元素: " + name)
        try:
            self.mini.page.get_element("[class='"+route+"']", max_timeout=3).tap()

        except IOError  as e:
            #self.mini.page.capture("F://桌面/assessment截图/" + route +'jpg')
            log.error('没有找到对应的元素：' + name + ";      报错信息是：" + str(e))


    def element_text(self, route,name):
        """获取元素文字"""
        strs=[]
        log.info("获取文字: " + name)
        try:
            strs=self.mini.page.get_element("[class='"+route+"']", max_timeout=3).text
            return  strs
        except IOError  as e:

            #self.mini.page.capture("F://桌面/assessment截图/" + route +'jpg')
            log.error('没有找到对应的元素：' + route + ";      报错信息是：" + str(e))
            return  strs


    def elements_text(self,i, route,name):
        """获取元素文字"""
        strs=[]
        log.info("获取文字: " + name)
        try:
            strs= str(self.mini.page.get_elements("[class='"+route+"']", max_timeout=3)[i].text)
            log.info("得到文字: " + strs)
            return  strs
        except IOError  as e:

            #self.mini.page.capture("F://桌面/assessment截图/" + route +'jpg')
            log.error('没有找到对应的元素：' + route + ";      报错信息是：" + str(e))
            return  strs


    def elements_shaow_text(self,i,name):
        """获取元素文字"""
        strs=[]
        log.info("获取文字: " + name)
        try:
            #strs= str(self.mini.page.get_elements("[class='"+route+"']", max_timeout=3)[i].text)
            strs = str(self.mini.page.get_element("view").get_elements("view")[1].get_elements("view")[i].get_element("text").text)
            log.info("得到文字: " + strs)
            return  strs
        except IOError  as e:

            #self.mini.page.capture("F://桌面/assessment截图/" + route +'jpg')
            log.error('没有找到对应的元素：' + name + ";      报错信息是：" + str(e))
            return  strs

    def  element_view_tap(self,name):

            try :
                lennum=len(self.mini.page.get_elements("view"))
                for i in range(0,lennum) :
                    if str(self.mini.page.get_elements("view")[i].text) == name:
                        self.mini.page.get_elements("view")[i].tap()
                        log.info("点击元素"+ name)

            except IOError as e:
                # self.mini.page.capture("F://桌面/assessment截图/" + route +'jpg')
                log.error('没有找到对应的元素：' + name + ";      报错信息是：" + str(e))


    def elements_text_exist(self,i, route,name):
        """获取元素文字"""
        strs=[]
        log.info("获取文字: " + name)
        try:
            strs=self.mini.page.get_elements("[class='"+route+"']", max_timeout=3)[i].text
            return  strs
        except IOError  as e:

            #self.mini.page.capture("F://桌面/assessment截图/" + route +'jpg')
            log.error('没有找到对应的元素：' + route + ";      报错信息是：" + str(e))
            return  strs






    def element_tap_image(self, route,name):
        """点击元素"""

        log.info("点击元素: " + name)
        try:
            self.mini.page.get_element("image[mode='"+route+"']", max_timeout=3).tap()

        except IOError  as e:
            #self.mini.page.capture("F://桌面/assessment截图/" + route +'jpg')
            log.error('没有找到对应的元素：' + name + ";      报错信息是：" + str(e))







    def element_tap_checkbox(self, i1,i2):
        """点击元素"""

        log.info("点击第"+str(i1+1) +"个多选框，点击选项第" + str(i2+1)+ "个选项")
        try:
            self.mini.page.get_elements("van-checkbox-group")[i1].get_elements("van-checkbox")[i2].get_element("view").get_element("van-icon").get_element("view").tap()

        except IOError  as e:
            #self.mini.page.capture("F://桌面/assessment截图/" + route +'jpg')
            log.error('没有找到第：' + str(i2+1) + "个选项;      报错信息是：" + str(e))


    def element_checkbox_num(self):
        num = self.mini.page.get_elements("van-checkbox-group") #获取多选框题的个数
        log.info('获取了' + str(len(num)) +'个多选框')
        return  len(num)

    def element_checkbox_nums(self,i):
        num = self.mini.page.get_elements("van-checkbox-group")[i].get_elements("van-checkbox") #获取多选框选项的个数
        log.info('获取了' + str(len(num)) +'个多选框选项')
        return  len(num)



    def element_radio_num(self):
        num = self.mini.page.get_elements("van-radio-group")#获取单选框题的个数
        log.info('获取了' + str(len(num)) +'个单选框')
        return len(num)

    def element_radio_nums(self,i):
        num = self.mini.page.get_elements("van-radio-group")[i].get_elements("van-radio")#获取单选框题的个数
        log.info('获取了' + str(len(num)) +'个单选框选项')
        return len(num)




    def element_input_num(self):
        num = self.mini.page.get_elements("van-cell") #获取输入框的个数
        log.info('获取了' + str(len(num)) +'个输入框')
        return  len(num)






    def element_tap_radio(self, i1,i2):
        """点击元素"""
        log.info("点击选项第" + str(i2+1)+ "个选项")

        try:
            self.mini.page.get_elements("van-radio-group")[i1].get_elements("van-radio")[i2].get_element("view").get_element("van-icon").get_element("view").tap()

        except IOError  as e:
            #self.mini.page.capture("F://桌面/assessment截图/" + route +'jpg')
            log.error('没有找到第：' + str(i2+1) + "个选项;      报错信息是：" + str(e))



    def element_tap_button(self, i1,name):
        """点击元素"""
        log.info("点击元素" +name )

        try:
            self.mini.page.get_elements("van-button")[i1].get_element("button").tap()

        except IOError  as e:
            #self.mini.page.capture("F://桌面/assessment截图/" + route +'jpg')
            log.error('没有找到元素：' + name + ";      报错信息是：" + str(e))





    def element_is_exists(self, name ):

        try:
            log.info("查找文字: " + name)
            #element = self.mini.page.get_element("view",inner_text=name, max_timeout=5)

            self.mini.page.get_element("view",text_contains=name, max_timeout=3)
            #element.tap()
            return True
        except IOError  as e:

            #self.mini.page.capture("F://桌面/assessment截图/" + name +'jpg')
            log.error('没有找到对应的文字：' + name +';     错误信息是：' + str(e))
            return False

    def elementtext_is_exists(self, name ):

        try:
            log.info("查找文字: " + name)
            #element = self.mini.page.get_element("view",inner_text=name, max_timeout=5)

            self.mini.page.get_element("text",text_contains=name, max_timeout=3)
            #element.tap()
            return True
        except IOError  as e:

            #self.mini.page.capture("F://桌面/assessment截图/" + name +'jpg')
            log.error('没有找到对应的文字：' + name +';     错误信息是：' + str(e))
            return False




    def shadow_input_text(self,i,test,name):

        try:
            log.info( name+"的输入框里输入文字: " + test)

            self.mini.page.get_elements("van-field")[i].get_element("van-cell").get_element("view").get_element("input").input(test)

            #self.mini.page.native().input_text(test)
        except AssertionError  as e:
            #self.mini.page.capture("F://桌面/assessment截图/" + test +'jpg')
            log.error('错误信息是：' + str(e))
            #self.mini.page.assertTrue(os.path.exists(path), "截图路径存在")


    def shadow_input_textarea(self,i,test,name):

        try:
            log.info( name+"的输入框里输入文字: " + test)

            self.mini.page.get_elements("van-field")[i].get_element("van-cell").get_element("view").get_element("textarea").input(test)

        except AssertionError  as e:
            #self.mini.page.capture("F://桌面/assessment截图/" + test +'jpg')
            log.error('错误信息是：' + str(e))
            #self.mini.page.assertTrue(os.path.exists(path), "截图路径存在")
