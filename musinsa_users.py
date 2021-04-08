#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pymysql
import random
from faker import Faker
fake =Faker('ko_KR')
Faker.seed(3);
db= pymysql.connect(host='localhost',user='root',password='root',db='musinsa')
curs =db.cursor()
seq = 995
for _ in range(6):
    while True:
        ssn=fake.ssn()
        if (ssn[2]=='0' and ssn[3]=='0') or (ssn[4]=='0' and ssn[5]=='0'):
            continue
        break
    if ssn[7]=='1' or ssn[7]=='2':
        birthday= '19'+ssn[0:2]+'-'+ssn[2:4]+'-'+ssn[4:6]
    elif ssn[7]=='3' or ssn[7]=='4':
        birthday= '20'+ssn[0:2]+'-'+ssn[2:4]+'-'+ssn[4:6]
    if ssn[7]=='1' or ssn[7]=='3':
        gender='M'
        height=random.randint(160,190)
        print(gender)
        print(height)
        if height >=190:
            size='2XL'
        elif height >=180:
            size='XL'
        elif height >=170:
            size='L'
        elif height >=170:
            size='M'
        elif height >=170:
            size='S'
        print(size)
    elif ssn[7]=='2' or ssn[7]=='4':
        gender = 'F'
        height=random.randint(150,180)
        print(gender)
        print(height)
        if height >=170:
            size='L'
        elif height >=160:
            size='M'
        elif height >=150:
            size='S'
        print(size)
    query = "INSERT IGNORE INTO users(seq, id, password, name,  cellphone,address, ssn, CI, DI, birthday, gender,height, size, join_date) VALUES("    +str(seq)+",'"+fake.email() +"','"    +fake.password(length=8, special_chars=False, upper_case=False)    +"','"    +fake.name()+"','"    +fake.phone_number() +"','"    +fake.address() +"','"    +ssn +"','-','-','"    +birthday+"','"    +gender+"','"+str(height)+"','"+size+"', '"    +str(fake.date_between(start_date='-10y', end_date='-2m'))+"');"
    ret=curs.execute(query)
    print(query)
    if ret == 1:
        seq += 1
    else:
        print("error",seq,"ret",ret)
db.commit()
db.close()


# In[18]:


import pymysql
from faker import Faker
fake =Faker('ko_KR')
Faker.seed(1234);
import random
for _ in range(6):
    while True:
        ssn=fake.ssn()
        if (ssn[2]=='0' and ssn[3]=='0') or (ssn[4]=='0' and ssn[5]=='0'):
            continue
        break
    if ssn[7]=='1' or ssn[7]=='2':
        birthday= '19'+ssn[0:2]+'-'+ssn[2:4]+'-'+ssn[4:6]
    elif ssn[7]=='3' or ssn[7]=='4':
        birthday= '20'+ssn[0:2]+'-'+ssn[2:4]+'-'+ssn[4:6]
    if ssn[7]=='1' or ssn[7]=='3':
        gender='M'
        height=random.randint(160,190)
        print(gender)
        print(height)
        if height >=190:
            size='2XL'
        elif height >=180:
            size='XL'
        elif height >=170:
            size='L'
        elif height >=170:
            size='M'
        elif height >=170:
            size='S'
        print(size)
    elif ssn[7]=='2' or ssn[7]=='4':
        gender = 'F'
        height=random.randint(150,180)
        print(gender)
        print(height)
        if height >=170:
            size='L'
        elif height >=160:
            size='M'
        elif height >=150:
            size='S'
        print(size)

