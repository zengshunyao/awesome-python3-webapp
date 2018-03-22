#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def t():
    print('ok............');
    return 0;


# num = callable(t);
# print(num);


def f(a, b=1, *args, d=0, **kv):
    print('a:%s' % str(a));
    print('b:%s' % str(b));
    print('args:%s' % str(args));
    print('d:%s' % str(d));
    print('kv:%s' % str(kv));

f(1,*(2,3,4),2,d=5,**{'f':1,'fb':2});

f(*(1,2,3,4),**{'d':34,'f':1,'fb':2});