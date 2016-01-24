from selenium import webdriver

from random import *

driver = webdriver.Firefox()

driver.get("http://www.humanmetrics.com/cgi-win/jtypes2.asp")

#driver.find_element_by_xpath(".//*[@id='c_qsts']/form/div[1]/div/label[1]").click()
list1=[]
for i in range(1,65):
    b=str(i)
    c=str(randint(1,4))
    a=".//*[@id='c_qsts']/form/div["+b+"]/div/label["+c+"]"
    print(i," = ",a)
    try:
      driver.find_element_by_xpath(a).click()
    except:
        list1.append(i)

driver.find_element_by_xpath(".//*[@id='btsub']").click()

print(list1)