from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://zzs.lessoald.cn/lots-web/seller/index.html#/marketing/coupon/list?active-name=published")
driver.find_element_by_css_selector(".popup-main a").click()
driver.find_element_by_css_selector("input#userNameId").send_keys("800202")
driver.find_element_by_css_selector("input[name='password']").send_keys("111111")
driver.find_element_by_css_selector('input#loginBtnId').click()
time.sleep(5)

while 1 == 1:
    try:
        driver.find_element_by_link_text("停用").click()
        driver.find_element_by_css_selector(".box-footer-sure-btn").click()
        time.sleep(2)
        driver.find_element_by_css_selector(".box-footer-close-btn").click()
    except:
     pass

    try:
        driver.find_element_by_link_text("停发").click()

        driver.find_element_by_css_selector(".box-footer-sure-btn").click()
        time.sleep(2)
        driver.find_element_by_css_selector(".box-footer-close-btn").click()
    except:
     pass
