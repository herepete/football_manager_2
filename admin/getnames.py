#!/usr/bin/python3.6
import pandas as pd
import numpy as np
import requests
# had help from
#https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column
#https://stackoverflow.com/questions/43590153/http-error-403-forbidden-when-reading-html
# bit more hacky as i need to add extra steps to get to page

#get data
url="https://names.mongabay.com/male_names_alpha.htm"
header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
r = requests.get(url, headers=header)
data=pd.read_html(r.text)

#clear data
data=data[0]
dataList = []
for index,row in data.iterrows():
    mylist=[row.Name]
    dataList.append(mylist)
#print data
print (dataList)
