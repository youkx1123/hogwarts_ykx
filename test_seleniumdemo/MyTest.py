import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.set_window_size(1440, 900)
driver.find_element(By.XPATH, '//*[@id="kw222"]').send_keys("aaa")
driver.find_element(By.XPATH, '//*[@id="su"]').click()
#driver.find_element(By.LINK_TEXT, "所有分类").click()
time.sleep(5)

