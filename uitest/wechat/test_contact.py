"""
聯繫人用例
"""
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:
    with open("I:/workspace/python-project/BackEnd14/datas/contactdata.yml", encoding="utf-8") as f:
        contactdata = yaml.safe_load(f)

    def setup_class(self):
        caps = {
            "platformName": "android",
            # "deviceName": "66J5T19110001875",
            "deviceName": "T3QDU15B04000723",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            # "dontStopAppOnReset": True,
            "skipServerInitialization": True,
            "skipDeviceInitialization": True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("name,sex,tel", contactdata)
    def test_addcontact(self, name, sex, tel):
        """
        1. 点击团队
        2. 下拉点击添加成员
        3. 点击手动输入添加
        4. 输入姓名、性别、手机号
        5. 点击保存
        6. 断言保存成功
        """
        self.driver.find_element(MobileBy.XPATH, "//*[@text='团队']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).scrollIntoView('
                                                        'new UiSelector().textContains("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{sex}']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/../*[@text='手机号']").send_keys(tel)

        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        assert "成功" in self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        sleep(2)
        self.driver.back()
        self.driver.back()
        sleep(2)

    def test_delcontact(self):

