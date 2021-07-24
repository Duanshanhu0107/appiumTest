from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

from douyinlib.MainActivity import MainActivity
from douyinlib.douyinbase import DouyinBase


class fristDef(DouyinBase):

    def start(self):
        self.basestart()

        # 如果有`青少年保护`界面，点击`我知道了`
        iknow = self.driver.find_elements_by_id("text3")
        if iknow:
            iknow.click()

        ma = MainActivity(self.driver)
        ma.comment()
        # 根据id定位搜索位置框，点击
        self.driver.find_element_by_id("expand_search").click()

        # 根据id定位搜索输入框，点击
        sbox = self.driver.find_element_by_id('search_src_text')
        sbox.send_keys('白月黑羽')
        # 输入回车键，确定搜索
        self.driver.press_keycode(AndroidKey.ENTER)

        # 选择（定位）所有视频标题
        eles = self.driver.find_elements_by_id("title")

        for ele in eles:
            # 打印标题
            print(ele.text)

        input('**** Press to quit..')
        self.driver.quit()


if __name__ == '__main__':
    go = fristDef()
    go.start()
