# 由于chrome识别不到雪球的webview，元素定位有问题，所以代码搞不定
from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFind():
    def setup(self):
        self.desire_cap = {
            "platformName": "android",
            "deviceName": "66J5T19110001875",
            # "deviceName": "T3QDU15B04000723",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            # "dontStopAppOnReset": True,
            "skipServerInitialization": True,
            "skipDeviceInitialization": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_browser(self):
        # self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        # self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        # current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        # print(current_price)
        # assert current_price > 200
        #
        # self.driver.back()

        sleep(2)
        self.driver.find_elements(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/tab_icon']")[3].click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']").click()
        sleep(10)
        a_locator = (MobileBy.XPATH,"//*[@id='Layout_app_3V4']/div/div/ul/li[1]/div[2]/h1")

        webview = self.driver.find_elements(MobileBy.CLASS_NAME,"android.webkit.WebView")
        # for i in range(5):
        #     print(self.driver.contexts)
        # self.driver.switch_to.context(self.driver.contexts[-1])
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(a_locator))
        self.driver.find_element(*a_locator).click()
        #
        # self.driver.find_element(MobileBy.ID,"phone-number").send_keys('13810110202')
        # self.driver.find_element(MobileBy.ID, "code").send_keys('1234')
        # self.driver.find_element(MobileBy.XPATH, "/html/body/div/div/div[2]/div/div[2]/h1").click()


