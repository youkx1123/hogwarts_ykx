from time import sleep

from sel_js9.base import Base

'''
打开百度图库网址：https://image.baidu.com
识别上传按钮
点击上传按钮
将本地的图片文件上传
'''
class TestFile(Base):
    def test_file_upload(self):
        self.driver.get('https://image.baidu.com')
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys('/Users/youxy/you用/照片/iQIYI/2019_08_30_23_30_IMG_3452.JPG')
        sleep(5)
