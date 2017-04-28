#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-28 23:28:49
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from core.server.wxauthorize import WxSignatureHandler
import tornado.web


"""
解析规则
"""
urlpatterns = [(r'/wxsignature', WxSignatureHandler),  # 微信签名
               ]
