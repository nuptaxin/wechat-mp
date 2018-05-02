# -*- coding: utf-8 -*-
#activate_this = '/root/renzx/wechat/py3/bin/activate_this.py'
#exec(open(activate_this).read())
import hashlib
import web
import time
import os
from lxml import etree
import pymysql
import requests
import json
import configparser
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
            reply_content = self.reply(content)
            self.data_save(to_user, from_user, msg_type, msg_id, reply_content, 1, time.localtime(time.time()))
            return self.render.reply_text(from_user,to_user,int(time.time()),reply_content)
        else:
            pass

    def data_save(self, from_user, to_user, msg_type, msg_id, content, direction, msg_time):
        db = self.read_db_config()
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

    def reply(self, content):
        if content == '?' or content == '？':
            reply_content = "帮助菜单：\r\n1000-扇贝单词\r\n2000-天气预报"
        elif content == '1000':
            reply_content = "帮助-扇贝单词菜单：\r\n1001-绑定扇贝账号\r\n1002-解绑扇贝账号\r\n1003-打卡排行榜\r\n1004-我的打卡\r\n1009-返回上一页"
        elif content == '2000':
            reply_content = '天气预报功能开发中，请稍后再试'
        else:
            reply_content = self.talks_robot(content)
        return reply_content

    def get_shanbay(self, content):
        return '扇贝功能开发中，敬请期待'

    def talks_robot(self, content):
        api_url = 'http://www.tuling123.com/openapi/api'
        apikey = '26cb4aee3a1b4035983b80160c0604f9'
        data = {'key': apikey,
                'info': content}
        req = requests.post(api_url, data=data).text
        replys = json.loads(req)['text']
        return replys

    def read_db_config(self):
        config = configparser.ConfigParser()
        config.read('config/mysql.properties')

        ip = config .get('mysql0', "ip")
        port = config .getint("mysql0", "port")
        username = config .get("mysql0", "username")
        password = config .get("mysql0", "password")

        return pymysql.connect(ip, username, password, "wechat", charset='utf8')

application = web.application(urls, globals())

if __name__ == '__main__':
    application.run()