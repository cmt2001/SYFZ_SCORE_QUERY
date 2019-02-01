#!/usr/bin/env python
# -*- coding: utf-8 -*-

#这里是服务系统相关的配置文件
DEBUG = False

# 应用的网址
HOST_URL = "http://domain.com"
# Web 页面的百度统计
BAIDU_ANALYTICS = ""

# 微信公众平台配置
APP_ID = ""
APP_SECRET = ""
TOKEN = ""
EncodingAESKey = ""

# 数据库
SQLALCHEMY_DATABASE_URI = "mysql://user:password@host/dbname?charset=utf8mb4"

# SimSimi key
SIMSIMI_KEY = ''

# 天气 API
WEATHER_PRIVATE_KEY = ''
WEATHER_APPID = ''

# PM2.5
PM2_5_TOKEN = ''

# 素材库图片 ID
MUSIC_THUMB_MEDIA_ID = ""

# 密码加解密 KEY
PASSWORD_SECRET_KEY = ''

# 学院内网代理
SCHOOL_LAN_PROXIES = {
    "http": "http://user:pass@ip:port/"
}

# 教务管理系统
SCHOOL_YEAR = ''
SCHOOL_TERM = ''
# 公网地址
JW_WAN_HOST = ''
JW_LOGIN_URL = JW_WAN_HOST + ''
JW_SCORE_URL = JW_WAN_HOST + ''
# 内网地址
JW_LAN_HOST = ''
JW_LOGIN_URL_LAN = JW_LAN_HOST + ''
JW_SCORE_URL_LAN = JW_LAN_HOST + ''

# 图书馆
# 公网地址
LIBRARY_WAN_HOST = ''
LIBRARY_LOGIN_URL = LIBRARY_WAN_HOST + ''
LIBRARY_RECORD_URL = LIBRARY_WAN_HOST + ''
# 内网地址
LIBRARY_LAN_HOST = ''
LIBRARY_LOGIN_URL_LAN = LIBRARY_LAN_HOST + ''
LIBRARY_RECORD_URL_LAN = LIBRARY_LAN_HOST + ''

# 学院新闻地址
SCHOOL_NEWS_URL = ''
