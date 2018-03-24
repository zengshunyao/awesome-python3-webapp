#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Michael Liao'

import os, sys, time, subprocess

# 观察者
from watchdog.observers import Observer
# 文件系统事件
from watchdog.events import FileSystemEventHandler


def log(s):
    print('[Monitor] %s' % s);


class MyFileSystemEventHander(FileSystemEventHandler):
    def __init__(self, fn):
        super(MyFileSystemEventHander, self).__init__()
        self.restart = fn;

    # 任何事件都触发 函数
    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            log('Python source file changed: %s' % event.src_path)
            self.restart()


# 全局变量 缓存进程 和启动文件
command = ['echo', 'ok']
process = None

# 杀进程
def kill_process():
    global process
    if process:
        log('Kill process [%s]...' % process.pid);
        process.kill();
        process.wait();
        log('Process ended with code %s.' % process.returncode);
        process = None;

# 新启动进程
def start_process():
    global process, command
    log('Start process %s...' % ' '.join(command));
    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)

# 重启
def restart_process():
    kill_process();
    start_process();

# 启动项目
def start_watch(path, callback):
    # 看门狗
    observer = Observer();
    # 设置 计划 监控当前目录文件变化
    observer.schedule(MyFileSystemEventHander(restart_process), path, recursive=True)  # 递归下去
    # 看门狗开始
    observer.start();

    log('Watching directory %s...' % path)
    #启动进程
    start_process();
    try:
        while True:
            time.sleep(0.5);
    except KeyboardInterrupt:
        observer.stop();
    observer.join();

# main方法启动
if __name__ == '__main__':
    argv = sys.argv[1:]
    if not argv:
        print('Usage: ./pymonitor your-script.py')
        exit(0);

    if argv[0] != 'python3':
        argv.insert(0, 'python3')

    command = argv;  # 你的脚本 app.py
    path = os.path.abspath('.');
    print('current abspath: %s' % path);
    start_watch(path, None);
