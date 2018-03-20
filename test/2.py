#!/usr/bin/python
# -*- coding: UTF-8 -*-
#####################################
##    created by basededato        ##
##    2017-9-27                    ##
#####################################

# 数据库连接-mysql
#引入mysqldb模块
import pymysql
#引入配置文件
import mysqlconn_cfg
#创建连接
conn= pymysql.connect(
        host  =mysqlconn_cfg.host,
        port  =mysqlconn_cfg.port,
        user  =mysqlconn_cfg.user,
        passwd=mysqlconn_cfg.passwd,
        db    =mysqlconn_cfg.db
       )
#打开游标
cur = conn.cursor()

#接收输入参数
row=(id1,name,age)=(raw_input("请输入编号："),raw_input("请输入姓名："),input("请输入年龄："))
#print (type(age))

#输入数据合法性判断
while age > 100 or age < 18 :
    age = input("年龄超出限制，请重新输入")

sql_insert = "insert into tb_emp (id1,name,age) values ("+id1+",'"+name+"',"+str(age)+")"
#占位符使用
#cur.execute('insert into tb_emp (id1,name,age) values (%s,%s,%s)',row)

sql_delete = "delete from tb_emp where id1 = 1"

sql_select = "select * from tb_emp"
#执行游标
try :
    cur.execute(sql_insert)
    cur.execute(sql_delete)
    conn.commit()
#异常捕获
except:
    conn.rollback()
    print("error")

#查询结果
reslut=cur.execute(sql_select);
msg=cur.fetchmany(reslut)
for i in msg:
    print i

cur.close()
conn.close()