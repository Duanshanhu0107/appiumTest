from DuanFrame.UIWindow import UIWindow


class MainActivity(UIWindow):

    def __init__(self, deiver):
        self.deiver = deiver

    def comment(self):
        # 根据id定位搜索位置框，点击
        self.driver.find_element_by_id(self=self, id_="user_avatar").click()
