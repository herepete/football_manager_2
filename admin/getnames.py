#!/usr/bin/python3.6
import pandas as pd
import numpy as np
import requests
import pdb
import csv
import os


# had help from
#https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column
#https://stackoverflow.com/questions/43590153/http-error-403-forbidden-when-reading-html
# bit more hacky as i need to add extra steps to get to page

#get data

#firstnames 
url="https://names.mongabay.com/male_names_alpha.htm"
header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
r = requests.get(url, headers=header)
data=pd.read_html(r.text)

#clear data
data=data[0]
dataList = []
for index,row in data.iterrows():
    #mylist=[row.Name]
    temprow=row.Name.capitalize()
    #dataList.append(mylist)
    dataList.append(temprow)
#print data
#print (dataList)

os.chdir("..")
os.system('rm firstnames.csv')
out = csv.writer(open("firstnames.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
out.writerow(dataList)

#surnames 
url="https://names.mongabay.com/data/1000.html"
header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
r = requests.get(url, headers=header)
data=pd.read_html(r.text)

os.system('rm surnames.csv')
#clear data
data=data[0]
#and again as in panda format
data=data[0]
dataList = []
for row in data:
    temprow=row.capitalize()
    dataList.append(temprow)

out = csv.writer(open("surnames.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
out.writerow(dataList)
