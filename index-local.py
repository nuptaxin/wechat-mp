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
import datetime
import logging
from shanbay import shanbay_data

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='wechat-mp.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

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
        logging.info(str_xml)
        content=xml.find("Content").text#获得用户所输入的内容
        msg_type=xml.find("MsgType").text
        msg_id = xml.find("MsgId").text
        from_user=xml.find("FromUserName").text
        to_user=xml.find("ToUserName").text
        self.data_save(from_user, to_user, msg_type, msg_id, content, 0, time.localtime(time.time()))
        if msg_type == 'text':
            reply_content = self.reply(from_user, content)
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

    def reply(self, from_user, content):
        if content == '?' or content == '？' or content == '190':
            reply_content = "帮助菜单：\r\n100-扇贝单词\r\n200-天气预报"
        elif content == '100'or content == '119'or content == '129'or content == '139':
            reply_content = "帮助-扇贝单词菜单：\r\n110-账号绑定\r\n120-打卡排行榜\r\n130-我的打卡\r\n190-返回上一页"
        elif content == '110':
            reply_content = "帮助-扇贝单词-账号绑定菜单：\r\n111-我的绑定信息\r\n112-绑定新账号\r\n113-解绑账号\r\n119-返回上一页"
        elif content == '111':
            resultList = shanbay_data.get_user_info(from_user)
            reply_content = '扇贝id 扇贝名称 微信id'
            for r in resultList:
                if r.valid==1:
                    reply_content += ' '.join(('\r\n', str(r.uid), self.none_name_handle(r.name), str(r.wechat_uid)))
        elif content == '112':
            reply_content = '回复 112#扇贝id 绑定扇贝账号'
        elif content.startswith('112#'):
            reply_content = shanbay_data.bind_user(content[4:],from_user)
        elif content == '113':
            reply_content = shanbay_data.unbind_user(from_user)
        elif content == '120':
            resultList = shanbay_data.get_stat(datetime.date.today())
            reply_content = '扇贝排行榜(月榜)\r\n名次 姓名 学习时长 学习单词数 打卡率'
            count =1
            for r in resultList:
                reply_content += ' '.join(('\r\n',str(count), r.name,str(r.study_time),str(r.study_word),str(r.checkin_rate)))
                count +=1
            reply_content += '\r\n\r\n121-日排行榜\r\n122-周排行榜\r\n123-月排行榜\r\n124-季排行榜\r\n125-年排行榜\r\n129-返回上一页'
        elif content == '121':
            resultList = shanbay_data.get_stat(datetime.date.today(),1)
            reply_content = '扇贝排行榜(日榜)\r\n名次 姓名 学习时长 学习单词数 打卡率'
            count =1
            for r in resultList:
                reply_content += ' '.join(('\r\n',str(count), r.name,str(r.study_time),str(r.study_word),str(r.checkin_rate)))
                count +=1
        elif content == '122':
            resultList = shanbay_data.get_stat(datetime.date.today(),2)
            reply_content = '扇贝排行榜(周榜)\r\n名次 姓名 学习时长 学习单词数 打卡率'
            count =1
            for r in resultList:
                reply_content += ' '.join(('\r\n',str(count), r.name,str(r.study_time),str(r.study_word),str(r.checkin_rate)))
                count +=1
        elif content == '123':
            resultList = shanbay_data.get_stat(datetime.date.today(),3)
            reply_content = '扇贝排行榜(月榜)\r\n名次 姓名 学习时长 学习单词数 打卡率'
            count =1
            for r in resultList:
                reply_content += ' '.join(('\r\n',str(count), r.name,str(r.study_time),str(r.study_word),str(r.checkin_rate)))
                count +=1
        elif content == '124':
            reply_content = '暂未推出扇贝排行榜季榜功能，敬请期待'
        elif content == '125':
            resultList = shanbay_data.get_stat(datetime.date.today(),5)
            reply_content = '扇贝排行榜(年榜)\r\n名次 姓名 学习时长 学习单词数 打卡率'
            count =1
            for r in resultList:
                reply_content += ' '.join(('\r\n',str(count), r.name,str(r.study_time),str(r.study_word),str(r.checkin_rate)))
                count +=1
        elif content == '130':
            reply_content = shanbay_data.get_user_stat(datetime.date.today(),from_user)
            reply_content += '\r\n\r\n139-返回上一页'
        elif content == '200':
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

        ip = config .get('wechat', "ip")
        port = config .getint("wechat", "port")
        username = config .get("wechat", "username")
        password = config .get("wechat", "password")
        database = config .get("wechat", "database")

        return pymysql.connect(ip, username, password, database, port, charset='utf8')

    def none_name_handle(self, name):
        if name is None:
            return '未命名'
        else:
            return name

application = web.application(urls, globals())

if __name__ == '__main__':
    application.run()