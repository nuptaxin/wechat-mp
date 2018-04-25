# -*- coding: UTF-8 -*-
activate_this = '/root/renzx/pythonWeb/ashin.ren/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import web
import hashlib
import os
import time
import urllib2, json
import xml.dom.minidom
import requests
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
        str_xml = web.data()
        #web.debug(os.sys.path)
        DOMTree = xml.dom.minidom.parseString(str_xml)
        root = DOMTree.documentElement
        msgId = root.getElementsByTagName("MsgId")[0].firstChild.data
        msgType = root.getElementsByTagName("MsgType")[0].firstChild.data
        content = root.getElementsByTagName('Content')[0].firstChild.data
        toUser = root.getElementsByTagName('ToUserName')[0].firstChild.data
        fromUser = root.getElementsByTagName('FromUserName')[0].firstChild.data
        web.debug('content:'+content)
        db = MySQLdb.connect("45.78.59.214", "usercount", "uc1234321", "wechat_py",charset="utf8")
        cursor = db.cursor()
        sql = """INSERT INTO wechat_msg(
                 tousername, fromusername, createtime, msgtype,content,funcflag, msgid)
                 VALUES ('%s', '%s',now(), %d, '%s',%d,'%s')""" % (toUser, fromUser, 0, content, 0, msgId)
        try:
            cursor.execute(sql)
            db.commit()
        except BaseException, e:
            db.rollback()
            web.debug(e)
        finally:
            db.close()
        if msgType == 'text':
            if content=='?' or content =='？'.decode('utf-8'):
                answer = "帮助菜单：\r\n1000-扇贝单词\r\n2000-天气预报"
            elif content=='1000':
                answer = self.get_shanbay(content)
            elif content=='2000':
                answer = '天气预报功能开发中，请稍后再试'
            else:
                answer = self.talks_robot(content)
            web.debug('answer:'+answer.decode('unicode_escape'))
            db = MySQLdb.connect("45.78.59.214", "usercount", "uc1234321", "wechat_py",charset="utf8")
            cursor = db.cursor()
            sql = """INSERT INTO wechat_msg(
                             tousername, fromusername, createtime, msgtype,content,funcflag,msgid)
                             VALUES ('%s', '%s',now(), %d, '%s',%d,'%s')""" % (
            fromUser,toUser, 0, answer, 1, msgId)
            try:
                cursor.execute(sql)
                db.commit()
            except BaseException, e:
                db.rollback()
                print e
            finally:
                db.close()
            return self.render.reply_text(fromUser, toUser, int(time.time()), answer)
        elif msgType == 'image':
            pass
        else:
            pass

    def talks_robot(self, info):
        api_url = 'http://www.tuling123.com/openapi/api'
        apikey = '26cb4aee3a1b4035983b80160c0604f9'
        data = {'key': apikey,
                'info': info}
        req = requests.post(api_url, data=data).text
        replys = json.loads(req)['text']
        return replys
    def get_shanbay(self, info):
        return '扇贝功能开发中，敬请期待'


application = web.application(urls, globals()).wsgifunc()