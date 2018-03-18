#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from www.orm import Model, StringField, IntegerField

#用户表
class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField();


# 创建实例:
user = User(id=123, name='Michael')
# 存入数据库:
user.insert()
# 查询所有User对象:
users = User.findAll()