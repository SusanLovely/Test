from appium import webdriver
import pytest


class TestXueQiu:

    def setup(self):
        desire_cap = {
            "platformName": "android",
            # "platformVersion": "5.1.1",
            # "deviceName": "T3QDU15B04000723",
            "deviceName": "66J5T19110001875",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        '''
        1. 打开雪球app
        2. 点击搜索输入框
        3. 输入阿里巴巴，选择阿里巴巴进行点击操作
        4. 获取阿里巴巴的股价，判定股价的价格大于200
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        print(current_price)
        assert current_price > 200
