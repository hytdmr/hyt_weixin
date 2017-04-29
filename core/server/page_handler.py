#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-29 23:07:48
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import tornado.web


class PageHandler(tornado.web.RequestHandler):
    """
微信handler处理类
    """

    def post(self, flag):
        if flag == 'index':
            '''首页'''
            self.render('index.html')
