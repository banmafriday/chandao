from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
url = 'http://zentao.lessoald.cn/zentao/user-login-L3plbnRhby9xYS5odG1s.html'
options = Options()
options.add_argument("--incognito")
options.add_argument('--headless')
driver = webdriver.Chrome(options=options, )
driver.get(url=url)
# print(driver.page_source[:300])

driver.find_element_by_css_selector('input#account').send_keys('wushanzhang')
driver.find_element_by_css_selector('input[name="password"]').send_keys('wsz13975943593')
driver.find_element_by_css_selector('button#submit').click()
time.sleep(6)
driver.find_element_by_css_selector('nav#navbar > ul > li:nth-of-type(4) > a').click()
time.sleep(6)
reuslt = driver.find_element_by_css_selector('div:nth-of-type(1) > .table-row > .col-7 > div:nth-of-type(1)'
                                             ' > .type-info > .type-value > strong > a')
print(reuslt.text+'未解决')

result1 = driver.find_element_by_css_selector('div:nth-of-type(1) > .table-row > .col-7 > div:nth-of-type(2)'
                                              ' > .type-info > .type-value > strong > a')
print(result1.text+'未确认')

result2= driver.find_element_by_css_selector('div:nth-of-type(1) > .table-row > .col-7 > div:nth-of-type(3)'
                                             ' > .type-info > .type-value > strong > a')
print(result2.text+'未关闭')
print(driver.title)
print(driver.current_url)
print(driver.add_cookie)
print(driver.current_url)
print("斑马")
driver.close()
driver.quit()
