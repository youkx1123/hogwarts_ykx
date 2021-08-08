from selenium import webdriver
from tmp.main import Main


class Testwait:
    def setup(self):
        main = Main()
        var = main.click_first_link.title()
