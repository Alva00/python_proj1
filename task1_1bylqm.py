
# coding: utf-8

# In[187]:


import urllib
import urllib2
import re
import pandas
import numpy
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame



# In[188]:


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


# In[189]:


#page_source.encode('unicode-escape').decode('string_escape')
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
    table = DataFrame(final,columns=colHead)
    return table


# In[190]:


def Data_Sort(dtframe,colHead,col):
    for i in range(len(dtframe[colHead[col]])):
        dtframe[colHead[col]][i] = float(dtframe[colHead[col]][i])
    dtframe = dtframe.sort_values(by=colHead[col])
    return dtframe

def metal_to_csv(dtframe,metal_name):
    dtframe = dtframe.loc[table[colHead[0]].str.contains(metal_name)]
    print dtframe
    dtframe.to_csv("metal_"+metal_name+"_data.csv",encoding="utf-8")


# In[191]:


if __name__ == "__main__":
   url = 'http://www.shfe.com.cn/statements/delaymarket_all.html'
   page_str = get_html(url)
   table = get_dtframe(page_str)
   colHead = table.columns.values.tolist()
   #table = Data_Sort(table,colHead,2)
   #print table
   #print table.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False) clean all none
   #print table.loc[table[colHead[4]].isnull()]
   table.sort_values(by=colHead[0])
   
   metal_list = ['ag','al','au','bu','cu','fu','hc','ni','pb','rb','ru','sn','wr','zn']
   for metal_name in metal_list: 
       metal_to_csv(table,metal_name)
   

