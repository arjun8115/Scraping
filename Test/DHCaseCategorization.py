from selenium import webdriver
from selenium.webdriver.support.ui import Select
import json

def funcCaseCategory():
    # driver = webdriver.Chrome(r"..\library\chromedriver.exe")
    driver = webdriver.PhantomJS(r"../library/phantomjs.exe");
    print("hello3")

    driver.get("http://delhihighcourt.nic.in/casecategorization.asp")


    list = driver.find_elements_by_xpath("//ul[contains(@class,'clearfix grid')]")

    temp = {}
    lst = []
    for item in list:

        list2 = item.find_elements_by_tag_name('span')
        tlst = []
        for item1 in list2:
            tlst.append(item1.text)
            #print(item1.text)
        lst.append(tlst)

    driver.get("http://delhihighcourt.nic.in/casecategorization.asp?currentPage=2")

    list = driver.find_elements_by_xpath("//ul[contains(@class,'clearfix grid')]")

    for item in list:

        list2 = item.find_elements_by_tag_name('span')
        tlst = []
        for item1 in list2:
            tlst.append(item1.text)
            #print(item1.text)
        lst.append(tlst)

    driver.get("http://delhihighcourt.nic.in/casecategorization.asp?currentPage=3")

    list = driver.find_elements_by_xpath("//ul[contains(@class,'clearfix grid')]")

    for item in list:

        list2 = item.find_elements_by_tag_name('span')
        tlst = []
        for item1 in list2:
            tlst.append(item1.text)
            #print(item1.text)
        lst.append(tlst)

    temp=json.dumps(lst)
    return temp
