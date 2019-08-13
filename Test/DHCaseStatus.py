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

def judgment(listNumber):
    listNo = listNumber  # should be given in %8 manner
    xpathStr = '//*[@id="InnerPageContent"]/ul/li[' + listNo + ']/span[2]/button'
    driver.find_element_by_xpath(xpathStr).click()
    list = driver.find_elements_by_xpath("//ul[contains(@class,'clearfix grid last')]")

    listUrl=[]
    for item in list:
        list2 = item.find_elements_by_tag_name('span')
        tlst = []
        list3 = item.find_elements_by_tag_name('button')
        xurl = ""
        for item1 in list3:
            xurl = item1.get_attribute('onclick')
            xurl = xurl[15:-1]
            listUrl.append(xurl)
        print(listUrl)

        for item1 in list2:
            tlst.append(item1.text)
            print(item1.text)
    temp = json.dumps(listUrl)
    return temp

def showStatusNextPage():
    lst= []
    listPage = driver.find_elements_by_xpath("//div[contains(@class,'page-navigation')]")
    sz = []
    for item in listPage:
        sz.append(item.text)
    le = len(sz[0])

    flag = "a"

    flag = "b"  # click on first page on "b"
    if flag == "b":
        judgment()

    if le > 10 and flag == "a":
        print("enter")
        pageNo = 8
        ur12 = ""
        for item in listPage:
            listPage2 = item.find_element_by_class_name("archivelink")
            url2 = listPage2.get_attribute('href')
        urlString = unquote(url2)
        while 1:
            prevListSize = len(lst)
            resultUrl = ""
        #    // *[ @ id = "InnerPageContent"] / div / a[1]   //*[@id="InnerPageContent"]/div/a[2]
            subst = "SRecNo="
            ind1 = urlString.find(subst)
            pageNoString = str(pageNo)
            ind2 = urlString.find("&dno")

            resultUrl += urlString[:ind1] + subst + pageNoString + urlString[ind2:]

            # print(resultUrl)

            driver.get(resultUrl)
            list = driver.find_elements_by_xpath("//ul[contains(@class,'clearfix grid')]")
            for item in list:
                list2 = item.find_elements_by_tag_name('span')
                tlst = []
                for item1 in list2:
                    tlst.append(item1.text)
                lst.append(tlst)

            listSize = len(lst)
            pageNo += 8

            flag = "a"

            flag = "b"  # click on that page
            if flag == "b":
                judgment()

            if lst[listSize - 1] == lst[prevListSize - 1] or flag == "b":
                break


def showStatus():
    list = driver.find_elements_by_xpath("//ul[contains(@class,'clearfix grid')]")
    temp = {}
    lst = []
    for item in list:
        list2 = item.find_elements_by_tag_name('span')
        tlst = []
        for item1 in list2:
            tlst.append(item1.text)
        lst.append(tlst)

    #temp = json.dumps(lst)
    return lst

def showStatusNext(pageno):
    print("next->page")
    path = '//*[@id="InnerPageContent"]/div/a[' +str(pageno)+ ']'

    driver.find_element_by_xpath(path).click()
    print("click")
    list = driver.find_elements_by_xpath("//ul[contains(@class,'clearfix grid')]")
    temp = {}
    lst = []
    for item in list:
        list2 = item.find_elements_by_tag_name('span')
        tlst = []
        for item1 in list2:
            tlst.append(item1.text)
        lst.append(tlst)

    temp = json.dumps(lst)
    return temp

def funcCaseType(casetype, No, year):
    #driver = webdriver.Chrome(r"C:\Users\Arjun Jaiswal\PycharmProjects\FirstSeleniumTest\library\chromedriver.exe")
    url = "http://delhihighcourt.nic.in/case.asp"
    driver.get(url)

    captcha = driver.find_element_by_xpath('//*[@id="InnerPageContent"]/form[1]/label[4]')
    subcaptcha = captcha.text[12:16]
    #print(subcaptcha)

    s1 = Select(driver.find_element_by_xpath('//*[@name="ctype_29"]'))
    #s1.select_by_value("ARB.P.")
    s1.select_by_value(casetype)

    s2 = driver.find_element_by_xpath('//*[@name="cno"]')
    s2.send_keys(No)

    s3 = Select(driver.find_element_by_xpath('//*[@name="cyear"]'))
    s3.select_by_value(year)

    s4 = driver.find_element_by_xpath('//*[@id="inputdigit"]')
    s4.send_keys(subcaptcha)

    driver.find_element_by_xpath('//button[@type="submit" and @class="pull-right"]').click()

    return showStatus()








def funcPetRes(pet,year):
    url = "http://delhihighcourt.nic.in/case.asp"
    driver.get(url)

    captcha = driver.find_element_by_xpath('//*[@id="InnerPageContent"]/form[1]/label[4]')
    subcaptcha = captcha.text[12:16]
    print(subcaptcha)

    s1 = driver.find_element_by_xpath('//*[@name="party"]')
    s1.send_keys(pet)

    s2 = Select(driver.find_element_by_xpath('//*[@name="pyear"]'))
    s2.select_by_value(year)

    s3 = driver.find_element_by_xpath('//*[@id="InnerPageContent"]/form[2]')
    s3.find_element_by_id("inputdigit").send_keys(subcaptcha)

    s4 = driver.find_element_by_xpath('//*[@id="InnerPageContent"]/form[2]')
    s4.find_element_by_class_name("pull-right").click()

    return showStatus()


def funAdvocate(adv,year):
    url = "http://delhihighcourt.nic.in/case.asp"
    driver.get(url)

    captcha = driver.find_element_by_xpath('//*[@id="InnerPageContent"]/form[1]/label[4]')
    subcaptcha = captcha.text[12:16]
    print(subcaptcha)

    s1 = driver.find_element_by_xpath('//*[@name="adv"]')
    s1.send_keys(adv)

    s2 = Select(driver.find_element_by_xpath('//*[@name="ayear"]'))
    s2.select_by_value(year)

    s3 = driver.find_element_by_xpath('//*[@id="InnerPageContent"]/form[3]')
    s3.find_element_by_id("inputdigit").send_keys(subcaptcha)

    s4 = driver.find_element_by_xpath('//*[@id="InnerPageContent"]/form[3]')
    s4.find_element_by_class_name("pull-right").click()

    return showStatus()

