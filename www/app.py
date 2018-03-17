#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging;

import asyncio;
import os;
import json;
import time;
from datetime import datetime;
from aiohttp import web;

logging.basicConfig(level=logging.INFO)

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>');


@asyncio.coroutine
def init(loop):
    #创建web对象 类是servlet
    app = web.Application(loop=loop);
    #增加  请求类型/映射路径/映射函数
    app.router.add_route('GET', '/', index);
    #异步创建Server object
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 8000);
    logging.info('server started at http://127.0.0.1:8000...')
    return srv;
    # pass;

#
eventLoop = asyncio.get_event_loop();
eventLoop.run_until_complete(init(eventLoop));
eventLoop.run_forever();
