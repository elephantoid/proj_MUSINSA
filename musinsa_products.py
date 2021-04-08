#!/usr/bin/env python
# coding: utf-8

# In[2]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
'https://store.musinsa.com/app/items/lists/001010/?category=&d_cat_cd=001010&u_cat_cd=&brand=&sort=sale_high&sub_sort=3m&display_cnt'


# In[3]:


import requests
import re


# In[4]:


def no_space(text):
    text1 = re.sub("&nbsp; | &nbsp;|\n|\t|\r","",text)
    text2 = re.sub("\n\n","",text1)
    return text2


# In[5]:


def get_text(url):
    item_name_list=[]
    item_price_list=[]
    try:
        html= urlopen(url)
        bs= BeautifulSoup(html, "html.parser")
        
        
        title = bs.findAll('p', {"class":"list_info"}, recurisive=False)
        for i in title:
            text = no_space(i.get_text())
            item_name_list.append(text)
            print(text)
            
        price = bs.findAll('p', {"class":"price"})
        for i in price:
            text2 = no_space(i.get_text())
            item_price_list.append(text2)
            print(text2)
    except:
        print("실패")


# In[116]:


def get_title(url):
    html= urlopen(url)
    bs= BeautifulSoup(html, "html.parser")
    i=0
    item_name_list=[]
    for item_name in bs.find_all('p', {"class":"list_info"}):
        item_name_list.append(no_space(item_name.get_text()))
    return item_name_list


# In[103]:


item_name_list


# In[18]:


import pymysql
#실제 제품별 번호는 001010, 002003 ...
CategoryId_list = [
    ['긴팔 티셔츠', 1010],
    ['슈트/블레이저', 2003],
    ['니트/스웨터', 1006],
    ['후드 티셔츠', 1004],
    ['맨투맨/스웨트셔츠',1005],
    ['데님 팬츠',3002],
    ['슈트 팬츠/슬랙스', 3008],
    ['기타 아우터', 2015],
    ['트레이닝/조거 팬츠',3004]
]
db = pymysql.connect(host='localhost', user='root', password='root', db='musinsa')
curs = db.cursor()
for i in range(len(CategoryId_list)):
    CategoryId = CategoryId_list[i][1]
    for k in range(1,4):
        Limit=k
        url= f"https://store.musinsa.com/app/items/lists/"        +'00'+ str(CategoryId)+'/?category=&d_cat_cd='+str(CategoryId)+f"&u_cat_cd=&brand=&sort=sale_high&sub_sort=3m&display_cntt=90&page={Limit}"
    #실제 제품의 항목번호를 위하여 00을 추가, 판매순으로 sorting
        html= urlopen(url)
        bs= BeautifulSoup(html, "html.parser")
        item_name_list=[]
        for item_name in bs.find_all('p', {"class":"list_info"}):
            item_name_list.append(no_space(item_name.get_text()))
            print(i, item_name_list)
        item_price_list=[]
        for item_price in bs.find_all('p',{"class":"price"}):
            item_price_list.append(no_space(item_price.get_text())[0:6])
            print(i, item_price_list)
        item_brand_list=[]
        for item_brand in bs.find_all('p',{"class":"item_title"}):
            item_brand_list.append(no_space(item_brand.get_text()))
            print(i, item_brand_list)
        for j in range(len(item_name_list)):
            query = "INSERT INTO products(name,brand, price, type, created_date) VALUES('"            + item_name_list[j]+"','"+item_brand_list[j]+"',"+item_price_list[j].replace(',','')+", '"            + CategoryId_list[i][0]+"', curdate());"
            curs.execute(query)
db.commit()
db.close


# In[17]:


len(item_brand_list)

