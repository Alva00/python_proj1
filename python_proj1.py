
# coding: utf-8

# In[46]:


import urllib
import urllib2
import re
import pandas
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame


# In[47]:


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


# In[48]:


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


# In[ ]:





# In[83]:


def Data_Sort(dtframe,colHead,col):
    for i in range(len(dtframe[colHead[col]])):
        if str(dtframe[colHead[col]][i]) == 'None':
            dtframe[colHead[col]][i] = '0'
        dtframe[colHead[col]][i] = float(dtframe[colHead[col]][i])
        
    dtframe = dtframe.sort_values(by=colHead[col])
    return dtframe


# In[93]:


if __name__ == "__main__":
    
    url = 'http://www.shfe.com.cn/statements/delaymarket_all.html'
    page_str = get_html(url)
    table = get_dtframe(page_str)
    colHead = table.columns.values.tolist()
    
    '''
    #sort
    tableOfUD = Data_Sort(table,colHead,2)
    tableOfUD.to_csv("涨跌.csv",encoding="utf-8")
    #table1 = table.loc[table[colHead[5]].notnull()]
    tableOfVT = Data_Sort(table,colHead,5)
    tableOfVT.to_csv("成交量.csv",encoding="utf-8")
    
    #select
    tableOfKP = table.loc[table[colHead[8]].notnull()]
    tableOfKP.to_csv("开盘.csv",encoding="utf-8")

    tableOfL = table.loc[table[colHead[9]].notnull()]
    tableOfL.to_csv("最低.csv",encoding="utf-8")
    
    
    tableOfH = table.loc[table[colHead[10]].notnull()]
    tableOfH.to_csv("最高.csv",encoding="utf-8")
   '''

    

