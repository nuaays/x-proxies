# coding: utf8

"""
    launcher.py: start web crawler service, flask api service.
"""
import os

import gevent
from gevent import monkey
from gevent import pywsgi

from api import web
from backend import scheduler

# checkout to project directory
project = os.path.split(os.path.realpath(__file__))[0]
os.chdir(project)

monkey.patch_all()


def master():
    """
    :return:
    """
    while True:
        gevent.sleep(600)


def loop():
    """
    :return:
    """
    gevent.joinall([gevent.spawn(master)])


if __name__ == '__main__':
    port = 5000
    http_server = pywsgi.WSGIServer(('', port), web.app)
    print('Running on http://127.0.0.1:%s' % port)
    gevent.spawn(http_server.start)
    scheduler.start()
    loop()
