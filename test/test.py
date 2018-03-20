# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

import www.orm
from www.models import User  # , Blog, Comment


@asyncio.coroutine
def test():
    yield from www.orm.create_pool(None, user='www-data', password='www-data', db='awesome');
    u = User(name='Test', email='test2@example.com', passwd='1234567890', image='about:blank');
    yield from u.save();
# await
# g=test();
# next(g);
for x in test():
    pass
