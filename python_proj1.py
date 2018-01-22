
# coding: utf-8

# In[8]:


import urllib
import urllib2
import re
import pandas
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame


# In[9]:


def get_html(url):
    user_agent = 'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Connection': 'keep-alive',
        'Referer': 'http://www.baidu.com/',
    }
    values = {
        'name': 'unkown',
        'location': 'Northampton',
        'language': 'Python'
    }
    data = urllib.urlencode(values)
    req = urllib2.Request(url,None,headers)
    response = urllib2.urlopen(req)
    page_source = response.read()
    return page_source


# In[12]:


def get_list(page_str):
    
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
    table = DataFrame(final,columns=colHead)
    
    for i in range(len(table[colHead[2]])):
        table[colHead[2]][i] = float(table[colHead[2]][i])
    table = table.sort_values(by=colHead[0])
    
    return table


# In[15]:


if __name__ == "__main__":
    
    url = 'http://www.shfe.com.cn/statements/delaymarket_all.html'
    page_str = get_html(url)
    final = get_list(page_str)

    final.to_csv("data.csv",encoding="utf-8")

