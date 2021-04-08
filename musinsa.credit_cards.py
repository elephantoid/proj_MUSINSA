#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
from faker import Faker
import pymysql
fake =Faker('ko_KR')
Faker.seed(234);

credit_card_type=[
    '하나 BC','비씨카드(페이북)', '제주카드', '씨티카드', '신협카드',
    '현대카드', '하나카드', 'KB증권(현대증권)',
    '하나(외환)', '신한카드','비씨카드','KDB산업', '카카오뱅크', '롯데카드', 'NH카드',
    '카카오뱅크카드', '삼성카드', '저축은행', '우리카드', 'MG새마을', 'KB 국민',
    'NH채움', 'SC은행카드', '케이뱅크', '광주카드', '수협카드', '전북카드', '수협카드'
]


db = pymysql.connect(host='localhost', user='root', password='root', db='musinsa')
curs = db.cursor()
seq = 0
for users_seq in range(1000):
    for _ in range(random.randint(1,3)):
        number= fake.credit_card_number()
        expiration_date = fake.credit_card_expire()
        cvc = fake.credit_card_security_code()
        name = fake.name()
        type1 = random.choice(credit_card_type)
        query = "INSERT INTO credit_cards(users_id, number, expiration_date, cvc, name, type)"        +"VALUES("+str(users_seq+1)+",'"+str(number)+"','"        +expiration_date +"',"+str(cvc)+", '"+name+"', '"+type1+"');"
        print(query)
        seq+=1
        curs.execute(query)
db.commit()
db.close
print(seq)

