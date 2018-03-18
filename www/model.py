#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from orm import Model;

class User(object):
    __table__='users';

    id = IntegerField(primary_key=True)
    name = StringField()