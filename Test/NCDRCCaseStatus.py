from selenium import webdriver
from selenium.webdriver.support.ui import Select
from urllib.parse import unquote
import json
#driver = webdriver.Chrome(r"C:\Users\Arjun Jaiswal\PycharmProjects\FirstSeleniumTest\library\chromedriver.exe")
driver = webdriver.PhantomJS(r"../library/phantomjs.exe")

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
#
# driver = webdriver.Chrome(options=options,
#                           executable_path=r'../library/chromedriver.exe')

def funcCaseType(caseNo):
    url = "http://cms.nic.in/ncdrcusersWeb/login.do?method=caseStatus"
    driver.get(url)

    s1 = driver.find_element_by_xpath('//*[@id="attachcase"]')
    s1.send_keys(caseNo)

    driver.find_element_by_xpath('//*[@id="srcbut"]').click()

    import time
    time.sleep(15)
    list = driver.find_elements_by_xpath('//*[@id="lblh5"]')
    hearing = ''
    for item in list:
        list2= item.find_elements_by_tag_name('td')
        for item1 in list2:
            hearing  = item1.text

    #driver.quit()
    return hearing