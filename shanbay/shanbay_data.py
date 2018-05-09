#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' module comment '

__author__ = 'Ashin Ren'

import calendar
import datetime
import pymysql
import configparser

def get_stat(data_date, data_type = 3):
    if data_type == 1:
        format_time = data_date.strftime('%Y-%m-%d %H:%M:%S')
    if data_type == 2:
        format_time = get_last_monday(data_date).strftime('%Y-%m-%d %H:%M:%S')
    if data_type == 3:
        format_time = data_date.strftime('%Y-%m')+'-1 00:00:00'
    if data_type == 5:
        format_time = data_date.strftime('%Y') + '-1-1 00:00:00'

    print(format_time)

    db = read_db_config()
    cursor = db.cursor()
    sql = '''select u.name,st.data_date,st.data_type,st.study_time,st.study_word,st.checkin_rate,st.integrity_rate,st.update_time from checkin_stat st, user_info u 
        where u.uid = st.uid and u.valid =1 and st.data_date='%s' and st.data_type = %d''' % (format_time, data_type)
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        resultList = []
        for row in results:
            name = row[0]
            data_date = row[1]
            data_type = row[2]
            study_time = row[3]
            study_word = row[4]
            checkin_rate = row[5]
            integrity_rate = row[6]
            update_time = row[7]
            # 打印结果
            tuple
            print("name=%s,data_date=%s,data_type=%d,study_time=%s,study_word=%d,checkin_rate=%d,integrity_rate=%d,update_time=%s" % \
                  (name, data_date, data_type, study_time, study_word, checkin_rate,integrity_rate, update_time))
            resultList.append(CheckinStat(name, study_time, study_word, checkin_rate))
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    resultList.sort( key=lambda obj:obj.checkin_rate, reverse=True)
    return resultList

def get_user_stat(data_date, wechat_uid):
    resultList = get_user_info(wechat_uid)
    if len(resultList)>0:
        for r in resultList:
            if r.valid==1:
                uid = r.uid
                break
            else:
                uid = None
        if uid is None:
            reply_content = '您未关联扇贝用户'
        else:
            day_date = data_date.strftime('%Y-%m-%d %H:%M:%S')
            week_date = get_last_monday(data_date).strftime('%Y-%m-%d %H:%M:%S')
            month_date = data_date.strftime('%Y-%m') + '-1 00:00:00'
            year_date = data_date.strftime('%Y') + '-1-1 00:00:00'

            date_map = {1:day_date,2:week_date,3:month_date,4:year_date}

            db = read_db_config()
            reply_content = '您的扇贝统计信息：'
            for (k,v) in date_map.items():
                print("key:"+str(k)+"\tvalue:"+str(v))
                k1 = int(k)
                v1 = str(v)
                cursor = db.cursor()
                sql = '''select st.data_date,st.data_type,st.study_time,st.study_word,st.checkin_rate,st.integrity_rate,st.update_time from checkin_stat st,user_info u
                                where u.uid = '%s' and u.valid =1 and st.uid = u.uid and st.data_date='%s' and st.data_type = '%d'
                                ''' % (uid,v1,k1)
                print(sql)
                try:
                    # 执行SQL语句
                    cursor.execute(sql)
                    # 获取所有记录列表
                    results = cursor.fetchall()
                    for row in results:
                        data_date = row[0]
                        data_type = row[1]
                        study_time = row[2]
                        study_word = row[3]
                        checkin_rate = row[4]
                        integrity_rate = row[5]
                        update_time = row[6]
                        # 打印结果
                        reply_content += '\r\n一个排行榜'+str(k1)
                        reply_content += ' '.join((str(study_time), str(study_word), str(checkin_rate)))
                except Exception as e:
                    print("Error: unable to fetch data")
                    print(e)
            # 关闭数据库连接
            db.close()
    else:
        reply_content = '您未关联扇贝用户'

    return reply_content

def get_last_monday(data_date):
    oneday = datetime.timedelta(days=1)
    while data_date.weekday() != calendar.MONDAY:
        data_date -= oneday
    return data_date

def get_user_info(wechat_uid):
    db = read_db_config()
    cursor = db.cursor()
    sql = '''SELECT
            u.id,
            u.uid,
            u.`name`,
            u.gender,
            u.birthday,
            u.valid,
            u.update_time,
            u.wechat_uid
            FROM
            user_info AS u
            WHERE
            u.wechat_uid = '%s'
            ''' % (wechat_uid)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        resultList = []
        for row in results:
            id = row[0]
            uid = row[1]
            name = row[2]
            gender = row[3]
            birthday = row[4]
            valid = row[5]
            update_time = row[6]
            wechat_uid = row[7]
            # 打印结果
            resultList.append(UserInfo(id, uid, name, gender, birthday, valid, wechat_uid))
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    #resultList.sort(key=lambda obj: obj.checkin_rate, reverse=True)
    return resultList

def bind_user(uid, wechat_uid):
    resultList = get_user_info(wechat_uid)
    if len(resultList)>0:
        for r in resultList:
            if r.valid==1:
                return'你已经绑定过扇贝id了，请勿重新绑定'
    db = read_db_config()
    cursor = db.cursor()
    sql = """INSERT INTO user_info
                     (uid, init, valid, update_time, wechat_uid) 
                     VALUES 
                     ('%s', '%d', '%d', now(), '%s')""" % (uid, 0, 1, wechat_uid)
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        reply_content = '恭喜你，绑定成功！'
    except:
        db.rollback()
        reply_content = '由于未知原因绑定失败'
    db.close()
    return reply_content

def unbind_user(wechat_uid):
    resultList = get_user_info(wechat_uid)
    if len(resultList) == 0:
        reply_content = '你未绑定过扇贝账号，无需解绑'
    else:
        for r in resultList:
            if r.valid==1:
                db = read_db_config()
                cursor = db.cursor()
                sql = """UPDATE user_info u set u.valid = 0,u.update_time = now() 
                          where u.id = '%d'""" % (r.id)
                print(sql)
                try:
                    cursor.execute(sql)
                    db.commit()
                    reply_content = '恭喜你，解绑成功！'
                except:
                    db.rollback()
                    reply_content = '由于未知原因解绑失败'
                db.close()
                break
            else:
                reply_content = '你已解绑过扇贝账号，无需解绑'

    return reply_content

def read_db_config():
    config = configparser.ConfigParser()
    config.read('config/mysql.properties')
    ip = config .get('shanbay', "ip")
    port = config .getint("shanbay", "port")
    username = config .get("shanbay", "username")
    password = config .get("shanbay", "password")
    database = config .get("shanbay", "database")
    return pymysql.connect(ip, username, password, database, port, charset='utf8')

class CheckinStat:
    def __init__(self, name, study_time, study_word, checkin_rate):
        self.name = name
        self.study_time = study_time
        self.study_word = study_word
        self.checkin_rate = checkin_rate

class UserInfo:
    def __init__(self, id, uid, name, gender, birthday, valid, wechat_uid):
        self.id = id
        self.uid = uid
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.valid = valid
        self.wechat_uid = wechat_uid



if __name__ == '__main__':
    #get_stat(datetime.date.today(),1)
    #get_stat(datetime.date.today(), 2)
    #get_stat(datetime.date.today(), 3)
    #get_stat(datetime.date.today(), 5)
    get_user_info()