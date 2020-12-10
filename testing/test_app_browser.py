from appium import webdriver
import time


class TestXueQiu:

    def setup(self):
        desire_cap = {
            "platformName": "android",
            # "platformVersion": "5.1.1",
            # "deviceName": "192.168.18.101:5555",
            # "platformVersion": "10",
            "deviceName": "66J5T19110001875",
            # "appPackage": "com.huawei.browser",
            "browserName": "Chrome",
            "noReset": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(3)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_url(self):
        self.driver.get("http://m.baidu.com")
        time.sleep(2)
