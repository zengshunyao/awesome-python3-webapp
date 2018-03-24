#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, time, subprocess

# 观察者
from watchdog.observers import Observer
# 文件系统事件
from watchdog.events import FileSystemEventHandler


def log(s):
    print('[Monitor] %s' % s);

# 全局变量 缓存进程 和启动文件
command = ['echo', 'ok']
process = None


class MyFileSystemEventHandler(FileSystemEventHandler):
    def __init__(self, fn):
        super(FileSystemEventHandler).__init__();
        self.restart = fn;

    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            log('Python source file changed: %s' % event.src_path)
            self.restart();

def start_watch(path, callback):
    observer = Observer();
    observer.schedule(MyFileSystemEventHandler(restart_process), path, recursive=True);
    observer.start();
    log('Watching directory %s...' % path)
    # 启动进程
    start_process();
    try:
        while True:
            time.sleep(0.5);
    except KeyboardInterrupt:
        observer.stop();#?
        kill_process();
    observer.join();#?

def kill_process():
    global process
    if process:
        log('Kill process [%s]...' % process.pid);
        process.kill();
        process.wait();
        log('Process ended with code %s.' % process.returncode);
        process = None;


def start_process():
    global process, command
    log('Start process %s...' % ' '.join(command));
    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr);

def restart_process():
    kill_process();
    start_process();

if __name__ == '__main__':
    argv = sys.argv[1:];
    if not argv:
        print('Usage: ./pymonitor your-script.py');
        exit(0);
    if argv[0] != 'python':
        argv.insert(0, 'python');

    print('argv:%s' % str(argv));
    command = argv;  # 你的脚本 app.py
    print('commond:%s'% str(command));
    path = os.path.abspath('.');
    print('current baspath:%s' % path);
    start_watch(path, None);
