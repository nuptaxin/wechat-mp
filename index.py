# -*- coding: utf-8 -*-
activate_this = '/root/renzx/wechat/py3/bin/activate_this.py'
exec(open(activate_this).read())
import hashlib
import web
import time
import os
from lxml import etree
import pymysql
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
        msg_type=xml.find("MsgType").text
        msg_id = xml.find("MsgId").text
        from_user=xml.find("FromUserName").text
        to_user=xml.find("ToUserName").text
        self.data_save(from_user, to_user, msg_type, msg_id, content, 0, time.localtime(time.time()))
        if msg_type == 'text':
            reply_content = "我现在还在开发中，还没有什么功能，您刚才说的是："+content
            self.data_save(to_user, from_user, msg_type, msg_id, reply_content, 1, time.localtime(time.time()))
            return self.render.reply_text(from_user,to_user,int(time.time()),"我现在还在开发中，还没有什么功能，您刚才说的是："+content)
        else:
            pass

    def data_save(self, from_user, to_user, msg_type, msg_id, content, direction, msg_time):
        db = pymysql.connect("localhost", "root", "root1234", "wechat", charset='utf8')
        cursor = db.cursor()
        sql = """INSERT INTO mp_msg
        (from_user, to_user, msg_type, msg_id, content, direction, msg_time, update_time) 
        VALUES 
        ('%s', '%s', '%s', '%s', '%s', '%d', '%s', now())""" % (from_user, to_user, msg_type, msg_id, content, direction, time.strftime("%Y-%m-%d %H:%M:%S", msg_time))
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()

application = web.application(urls, globals()).wsgifunc()