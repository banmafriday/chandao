from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://172.16.100.83:8080/tplus/view/portal/portal.html?t=1632898918619")
import time

time.sleep(30)
driver.find_elements_by_xpath("//li[@id='toolbarContainer-gp-More']/a/span/span").click()

time.sleep(2)
driver.find_elements_by_xpath("//li[@id='toolbarContainer-gp-More']/a/span/span").click()
time.sleep(2)
driver.find_elements_by_xpath("//li[@id='toolbarContainer-gp-More-grp-ul-Copy']/a/span/span[2]").click()
