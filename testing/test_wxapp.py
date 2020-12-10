import time

from appium import webdriver
# from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class TestWXMicro:
    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "66J5T19110001875",
            "appPackage": "com.tencent.mm",
            "appActivity": "com.tencent.mm.ui.LauncherUI",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "chromeOptions": {"androidProcess": "com.tencent.mm:appbrand0"},
            "adbPort": 5038,
            "dontStopAppOnReset": True,
            "skipServerInitialization": True,
            "skipDeviceInitialization": True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

        self.driver.find_element(By.XPATH, "//*[@text='通讯录']")
        self.driver.implicitly_wait(30)

    def test_search(self):
        # 原生自动化测试
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.4, size['width'] * 0.5, size['height'] * 0.8)
        # self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').click()
        # self.driver.find_element_by_name("取消")
        # self.driver.find_element(By.CLASS_NAME, "android.widget.EditText").send_keys("雪球")
        print(self.driver.contexts)
        self.driver.find_element(By.XPATH, "//*[@text='雪球']").click()
        #self.driver.find_element(By.XPATH, "//*[@text='自选']")
        self.driver.implicitly_wait(20)

        print(self.driver.contexts)
        self.driver.find_element(By.XPATH, "//*[@text='热门']").click()
        print(self.driver.contexts)

        # # 进入webview
        # self.driver.switch_to.context('e6db8f41-c4ff-4833-9829-20a927893aea')
        # self.driver.implicitly_wait(10)
        # self.find_top_window()
        #
        # # css定位
        # self.driver.find_element(By.CSS_SELECTOR, "[src*=stock_add]").click()
        # # 等待新窗口
        # WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 2)
        # self.find_top_window()
        # self.driver.find_element(By.CSS_SELECTOR, "._input").click()
        # # 输入
        # self.driver.switch_to.context("NATIVE_APP")
        # ActionChains(self.driver).send_keys("alibaba").perform()
        # # 点击
        # self.driver.switch_to.context('WEBVIEW_xweb')
        # self.driver.find_element(By.CSS_SELECTOR, ".stock__item")
        # self.driver.find_element(By.CSS_SELECTOR, ".stock__item").click()

    def find_top_window(self):
        windows = self.driver.window_handles
        for window in windows:
            if ":VISIBLE" in self.driver.title:
                return True
            else:
                self.driver.switch_to.window(window)
        return False
