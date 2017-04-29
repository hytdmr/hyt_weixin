#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-28 23:29:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from core.url import urlpatterns
from core.server.wxschedule import WxSchedule


define('port', default=8000, help='run on the given port', type=int)


class Application(tornado.web.Application):

    def __init__(self):
        settings = dict(
            template_path=os.path.join(
                os.path.dirname(__file__), "core/template"),
            static_path=os.path.join(os.path.dirname(__file__), "core/static"),
            debug=False,
            login_url="/login",
            cookie_secret="MuG7xxacQdGPR7Svny1OfY6AymHPb0H/t02+I8rIHHE="
        )
        super(Application, self).__init__(urlpatterns, **settings)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    wx_schedule = WxSchedule()
    wx_schedule.excute()
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
