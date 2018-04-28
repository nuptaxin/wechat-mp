# -*- coding: utf-8 -*-
#activate_this = '/root/renzx/wechat/py3/bin/activate_this.py'
#exec(open(activate_this).read())
import hashlib
import web
import time
import os
from lxml import etree
urls = (
    '/', 'hello',
    '/weixin', 'WeixinInterface'
)

class hello:
    def GET(self):
        return "Hello, linuxtone."


class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = "renzhengxin"
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return echostr

    def POST(self):
        str_xml = web.data() #获得post来的数据
        #web.debug(os.sys.path)
        xml = etree.fromstring(str_xml)#进行XML解析
        content=xml.find("Content").text#获得用户所输入的内容
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        if msgType == 'text':
            return self.render.reply_text(fromUser,toUser,int(time.time()),"我现在还在开发中，还没有什么功能，您刚才说的是："+content)
        else:
            pass

application = web.application(urls, globals())

if __name__ == '__main__':
    application.run()