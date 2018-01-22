
# coding: utf-8

# In[109]:


import urllib
import urllib2
import requests
import csv
import random
import time
import socket
from pandas.core.frame import DataFrame
from bs4 import BeautifulSoup
url = 'http://www.shfe.com.cn/statements/delaymarket_all.html'
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
    'name':'unkown',
    'location':'Northampton',
    'language':'Python'
}
data = urllib.urlencode(values)
req = urllib2.Request(url,None,headers)
response = urllib2.urlopen(req)
page_source = response.read()
print(page_source)


# In[163]:


final = []
bs = BeautifulSoup(page_source, "html.parser") 
table = bs.table
tr = table.find_all('tr')
for cnt in tr:
    td = cnt.find_all('td')
    temp = []
    for cntt in td:
        
        temp.append(cntt.string)
        
    final.append(temp)

final = final[1:]


# In[232]:


Final_Data = DataFrame(final)
#Final_Data.dtypes
a = 0
len(Final_Data[2])
for temple in range(138):
    Final_Data[2][temple+1] = float(Final_Data[2][temple+1])
Final_Data.sort_values(by=2)



# In[227]:


print Final_Data


# In[63]:


Final_Data.to_csv("data.csv",encoding="utf-8")
df = pandas.read_csv("data.csv",encoding="utf-8")
print df

