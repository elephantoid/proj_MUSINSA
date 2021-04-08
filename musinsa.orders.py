#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pymysql
import random
from faker import Faker
import datetime
db= pymysql.connect(host='localhost',user='root',password='root',db='musinsa')
curs = db.cursor(pymysql.cursors.DictCursor)
query = "select id, price from products"
curs.execute(query)
rows = curs.fetchall()
query2 = "select seq, users_id from credit_cards"
curs.execute(query2)
rows2 = curs.fetchall()
db.close()

delivery_time_type =['10:00','11:00','14:00','17:00','18:00','23:59']
start = datetime.datetime(2020, 9, 7, 12, 0, 0)
end =datetime.datetime(2020, 11, 7, 12, 0, 0)
fake = Faker('ko_KR')

credit_seq_list=[]
for i in range(1, 1001):
    line= []
    for row2 in rows2:
        if i == row2['users_id']:
            line.append(row2['seq'])
    credit_seq_list.append(line)

orders_id_users_seq= []
orders_id= 1
for i in range(1, 200):
    for _ in range(random.randint(4,12)):
        orders_id_users_seq.append([i, orders_id])
        orders_id +=1
for i in range(201, 1001):
    for _ in range(random.randint(1,4)):
        orders_id_users_seq.append([i, orders_id])
        orders_id +=1
last_orders_id = orders_id-1
print('마지막 주문 번호: ', last_orders_id)
orders_id_list = list(range(1, orders_id))
random.shuffle(orders_id_list)


# In[9]:


import pymysql
import random
from faker import Faker
import datetime
Faker.seed(3);
db= pymysql.connect(host='localhost',user='root',password='root',db='musinsa')
curs = db.cursor(pymysql.cursors.DictCursor)
query = "select id, price from products"
curs.execute(query)
rows = curs.fetchall()
query2 = "select seq, users_id from credit_cards"
curs.execute(query2)
rows2 = curs.fetchall()
db.close()

delivery_time_type =['10:00','11:00','14:00','17:00','18:00','23:59']
start = datetime.datetime(2020, 9, 7, 12, 0, 0)
end =datetime.datetime(2020, 11, 7, 12, 0, 0)
fake = Faker('ko_KR')

credit_seq_list=[]
for i in range(1, 1001):
    line= []
    for row2 in rows2:
        if i == row2['users_id']:
            line.append(row2['seq'])
    credit_seq_list.append(line)

orders_id_users_seq= []
orders_id= 1
#롱 테일 법칙
for i in range(1, 200):
    for _ in range(random.randint(4,15)):
        orders_id_users_seq.append([i, orders_id])
        orders_id +=1
for i in range(201, 1001):
    for _ in range(random.randint(1,4)):
        orders_id_users_seq.append([i, orders_id])
        orders_id +=1
last_orders_id = orders_id-1
print('마지막 주문 번호: ', last_orders_id)
orders_id_list = list(range(1, orders_id))
random.shuffle(orders_id_list)

users_id =0
for i in range(0,500):
    for j in range(last_orders_id):
        if orders_id_list[i] == orders_id_users_seq[j][1]:
            users_id = orders_id_users_seq[j][0]
    order_time = fake.date_time_between_dates(datetime_start=start, datetime_end=end)
    min_total_price = random.randint(30000,150000)
    total_price=0
    while total_price < min_total_price:
        products_id = random.randint(1,271)
        products_quantity = random.randint(1,3)
        total_price +=rows[products_id-1]['price']*products_quantity
        query4 = "INSERT INTO carts(orders_id, products_id, products_quantity)"                +" VALUES("+str(orders_id_list[i])+","+str(products_id)+","                +str(products_quantity)+");";
    credit_cards_seq = random.choice(credit_seq_list[users_id-1])
    delivery_day = random.randint(1,6)
    delivery_time = random.choice(delivery_time_type)
    query3 = "INSERT INTO orders(id, users_seq, time, total_price, credit_cards_seq, delivery_day, delivery_time)"            +" VALUES("+str(orders_id_list[i])+", "+str(users_id)+", '"+str(order_time)+"', "            +str(total_price)+", "+str(credit_cards_seq)+", "+str(delivery_day)+", '"            +delivery_time+"');";
for i in range(500,1000):
    for j in range(last_orders_id):
        if orders_id_list[i] == orders_id_users_seq[j][1]:
            users_id = orders_id_users_seq[j][0]
    order_time = fake.date_time_between_dates(datetime_start=start, datetime_end=end)
    min_total_price = random.randint(50000,150000)
    total_price=0
    while total_price < min_total_price:
        products_id = random.randint(721,900)
        products_quantity = random.randint(1,3)
        total_price +=rows[products_id-1]['price']*products_quantity
        query4 = "INSERT INTO carts(orders_id, products_id, products_quantity)"                +" VALUES("+str(orders_id_list[i])+","+str(products_id)+","                +str(products_quantity)+");";
    credit_cards_seq = random.choice(credit_seq_list[users_id-1])
    delivery_day = random.randint(1,6)
    delivery_time = random.choice(delivery_time_type)
    query3 = "INSERT INTO orders(id, users_seq, time, total_price, credit_cards_seq, delivery_day, delivery_time)"            +" VALUES("+str(orders_id_list[i])+", "+str(users_id)+", '"+str(order_time)+"', "            +str(total_price)+", "+str(credit_cards_seq)+", "+str(delivery_day)+", '"            +delivery_time+"');";
for i in range(1000,3000):
    for j in range(last_orders_id):
        if orders_id_list[i] == orders_id_users_seq[j][1]:
            users_id = orders_id_users_seq[j][0]
    order_time = fake.date_time_between_dates(datetime_start=start, datetime_end=end)
    min_total_price = random.randint(30000,80000)
    total_price=0
    while total_price < min_total_price:
        products_id = random.randint(1,2430)
        products_quantity = random.randint(1,3)
        total_price +=rows[products_id-1]['price']*products_quantity
        query4 = "INSERT INTO carts(orders_id, products_id, products_quantity)"                +" VALUES("+str(orders_id_list[i])+","+str(products_id)+","                +str(products_quantity)+");";
    credit_cards_seq = random.choice(credit_seq_list[users_id-1])
    delivery_day = random.randint(1,6)
    delivery_time = random.choice(delivery_time_type)
    query3 = "INSERT INTO orders(id, users_seq, time, total_price, credit_cards_seq, delivery_day, delivery_time)"            +" VALUES("+str(orders_id_list[i])+", "+str(users_id)+", '"+str(order_time)+"', "            +str(total_price)+", "+str(credit_cards_seq)+", "+str(delivery_day)+", '"            +delivery_time+"');";
for i in range(3000,orders_id-1):
    for j in range(last_orders_id):
        if orders_id_list[i] == orders_id_users_seq[j][1]:
            users_id = orders_id_users_seq[j][0]
            #print("[users_id]", orders_id_users_seq[j][0])
            #print("[orders_id]", orders_id_users_seq[j][1])
    order_time = fake.date_time_between_dates(datetime_start=start, datetime_end=end)
    min_total_price = random.randint(20000,300000)
    #print("\n**",i+1," 주문번호:", orders_id_list[i],"[min_total_price]", min_total_price, "원")
    total_price=0
    while total_price < min_total_price:
        products_id = random.randint(1,2430)
        priducts_quantity = random.randint(1,2)
        #print("\n상품 번호:", products_id)
        #print("상품 가격:",rows[products_id-1]["price"],"원")
        #print("수량:", priducts_quantity,"개")
        #print("상품 가격 * 수량:", rows[products_id-1]["price"]*priducts_quantity,"원")
        total_price += rows[products_id-1]['price']*priducts_quantity
        query4 ="INSERT INTO carts(orders_id,products_id,products_quantity)"               +"VALUES("+str(orders_id_list[i])+","+str(products_id)+","               +str(products_quantity)+");";
        print(query4)
    #print("\n[총 주문가격]",total_price,"원")
    credit_cards=seq = random.choice(credit_seq_list[users_id-1])
    delivery_day = random.randint(1,6)
    delivery_time = random.choice(delivery_time_type)
    query3="INSERT INTO orders(id, users_seq,time, total_price, credit_cards_seq, delivery_day, delivery_time)"    +"VALUES("+str(orders_id_list[i])+","+str(users_id)+",'"+str(order_time)+"',"    +str(total_price)+","+str(credit_cards_seq)+","+str(delivery_day)+",'"    +delivery_time+"');";
    print(query3)
print(orders_id_users_seq)

