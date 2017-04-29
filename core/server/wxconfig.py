#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-29 20:34:53
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class WxConfig(object):
    """
    微信开发--基础配置
    """

    AppID = 'wxda6c469182539e37'  # AppId(应用ID)
    AppSecret = 'af3110870983177f9913d02b545b3cb5'  # App_secret(应用密钥)

    AppHost = 'http://hytdmr.top'

    '''获取access_token'''
    config_get_access_token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
        AppID, AppSecret)

    '''自定义菜单创建接口'''
    menu_create_url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token='

    '''自定义菜单查询接口'''
    menu_get_url = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token='

    '''自定义菜单删除接口'''
    menu_delete_url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token='

    '''微信公众号菜单映射数据'''
    """重定向后会带上state参数，开发者可以填写a-zA-Z0-9的参数值，最多128字节"""
    wx_menu_state_map = {
        'nemuIndex0': '%s/page/index' % AppHost,  # 测试菜单1
    }
