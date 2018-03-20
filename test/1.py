#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        print('b=%s' % b);
        yield b
        a, b = b, a + b
        index += 1


print('-' * 10 + 'test yield fib' + '-' * 10)
for fib_res in fib(20):
    print(fib_res)