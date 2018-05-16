#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

sfid=''
openid=''

url='http://club.shimaogroup.com/m/Luckdraw/handler/SignHandler.ashx?type=suijinum'
values ={ 'sfid':sfid,'openid':openid }
#准备一下头
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
}
#将字典格式化成能用的形式
data = urllib.parse.urlencode(values).encode('utf-8')
#创建一个request,放入我们的地址、数据、头
request = urllib.request.Request(url, data, headers)
#访问
html = urllib.request.urlopen(request).read().decode('utf-8')
#利用json解析包解析返回的json数据 拿到翻译结果
jsondata = json.loads(html)
if jsondata['code']== 0:
    logger.info('签到成功'+'【'+html+'】')
    print('签到成功')
elif jsondata['code'] == 1 :
    logger.info('已经签到'+'【'+html+'】')
    print('已经签到')
else :
    logger.info('异常'+'【'+html+'】')
    print('已经签到')
