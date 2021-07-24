from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

from DuanFrame.UIWindow import UIWindow


class DouyinBase(object):

    def __init__(self, appPackage='com.ss.android.ugc.aweme', appActivity='.splash.SplashActivity'):
        self.platformVersion = '10'  # 手机安卓版本
        self.appPackage = appPackage  # 启动APP Package名称
        self.appActivity = appActivity  # 启动Activity名称

    def basestart(self):
        desired_caps = {
            'platformName': 'Android',  # 被测手机是安卓
            'platformVersion': self.platformVersion,
            'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
            'appPackage': self.appPackage,  # 启动APP Package名称
            'appActivity': '.splash.SplashActivity',  # 启动Activity名称
            'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
            'resetKeyboard': True,  # 执行完程序恢复原来输入法
            'noReset': False,  # 不要重置App
            'newCommandTimeout': 6000,
            'automationName': 'UiAutomator2'
            # 'app': r'd:\apk\bili.apk',
        }

        # 连接Appium Server，初始化自动化环境
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 设置缺省等待时间
        self.driver.implicitly_wait(5)

