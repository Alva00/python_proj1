import urllib
import urllib2
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from pandas.core.frame import DataFrame



def get(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    time.sleep(1)
    driver.switch_to.frame("smsg")
    content = driver.page_source.encode('utf-8')
    return content


def get_dtframe(page_str):
    final = []
    bs = BeautifulSoup(page_str, "html.parser")
    table = bs.table
    tr = table.find_all('tr')
    for cnt in tr:
        td = cnt.find_all('td')
        temp = []
        for cntt in td:
            temp.append(cntt.string)
        final.append(temp)
    colHead = final[1]
    final = final[2:]
    table = DataFrame(final, columns=colHead)
    return table


def Data_Sort(dtframe, colHead, col):
    for i in range(len(dtframe[colHead[col]])):
        if str(dtframe[colHead[col]][i]) == 'None':
            dtframe[colHead[col]][i] = '0'
        dtframe[colHead[col]][i] = float(dtframe[colHead[col]][i])

    dtframe = dtframe.sort_values(by=colHead[col])
    return dtframe


if __name__ == "__main__":
    url = 'http://www.shfe.com.cn/statements/dataview.html?paramid=delaymarket_all'
    page_str = get(url)
    table = get_dtframe(page_str)
    colHead = table.columns.values.tolist()
