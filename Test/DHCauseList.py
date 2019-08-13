from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
import json


#driver = webdriver.Chrome(r"..\library\chromedriver.exe")



#driver.set_page_load_timeout("10")

def funcCauseList(month,day,year):
    url = "http://delhihighcourt.nic.in/personalCauselist.asp"

    driver = webdriver.PhantomJS(r"../library/phantomjs.exe");
    print("hello1")
    driver.get(url)


    s1 = Select(driver.find_element_by_xpath('//*[@id="drpMonth"]'))
    s1.select_by_value(month)

    s2 = Select(driver.find_element_by_xpath('//*[@id="drpDay"]'))
    s2.select_by_value(day)

    s3 = Select(driver.find_element_by_xpath('//*[@id="drpYear"]'))
    s3.select_by_value(year)

    print("form filled")
    driver.find_element_by_xpath('//*[@id="criteria" and @value="FULL"]').click()

    driver.find_element_by_xpath('//input[@type="submit" and @value="Submit"]').click()


    list = driver.find_elements_by_xpath("//tr[contains(@class,'tabletxt')]")

    a=0
    temp = {}
    lst = []
    for item in list:
        List2 = item.find_elements_by_tag_name('td')
        tlst= []
        for item1 in List2:
            tlst.append(item1.text)
            a+=1
            if a>100:
             break
        lst.append(tlst)
    temp = json.dumps(lst)
    return temp


