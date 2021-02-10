from numpy.distutils.fcompiler import none
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = "https://work.weixin.qq.com/"

    def __init__(self, driver: webdriver = None) -> object:
        """

        :rtype: object
        """
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
