#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 读取店铺
path = "/data/datax"
fconfig = open("config.ini")
ftest = open("do.txt", "w")
config = fconfig.read()
config = config.strip("\n\r").strip()
print config
# 找到json配置文件模板，并替换内容
fjson = open("/Users/devil/Downloads/project/doc/datax.json.a")
dataj = fjson.read()
dataj = dataj.replace("table-place", "erp_trade_11")
dataj = dataj.replace("shop-id-place", config)
print dataj
# 关闭文件
fconfig.close()
ftest.close()