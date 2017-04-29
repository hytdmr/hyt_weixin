#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-29 20:11:04
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from core.cache.basecache import BaseCache
from core.logger_helper import logger


class TokenCache(BaseCache):
    """
微信Token缓存

set_cache  添加redis
get_cache  获取redis
    """

    _expire_access_token = 7200  # 微信access_token过期时间，2小时
    _expire_js_token = 30 * 24 * 3600  # 信息js网页授权过期时间，30天
    KEY_ACCESS_TOKEN = 'access_token'  # 微信全局唯一票据access_token
    KEY_JSAPI_TIKET = 'jsapi_ticket'  # JS_SDK授权签名的js_api_ticket

    def set_access_cache(self, key, value):
        '''添加微信access_token验证相关redis'''
        res = self.redis_ctl.set(key, value)
        self.redis_ctl.expire(key, self._expire_access_token)
        logger.debug(
            '【微信access_token缓存】setCache>>>key[' + key + '], value[' + value + ']')
        return res

    def set_js_cache(self, key, value):
        '''添加网页授权验证相关redis'''
        res = self.redis_ctl.set(key, value)
        self.redis_ctl.expire(key, self._expire_js_token)
        logger.debug(
            '【微信js_token缓存】setCache>>>key[' + key + '], value[' + value + ']')
        return res

    def get_cache(self, key):
        '''获取redis'''
        try:
            value = (self.redis_ctl.get(key)).decode('utf-8')
            logger.debug(value)
            logger.debug(
                '【微信token缓存】setCache>>>key[' + key + '], value[' + value + ']')
            return value
        except Exception:
            return None
