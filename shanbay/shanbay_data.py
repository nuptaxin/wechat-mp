#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' module comment '

__author__ = 'Ashin Ren'

import time
import calendar
import datetime
import pymysql

def get_stat(data_date, data_type):
    if data_type == 1:
        format_time = data_date.strftime('%Y-%m-%d %H:%M:%S')
    if data_type == 2:
        format_time = get_last_monday(data_date).strftime('%Y-%m-%d %H:%M:%S')
    if data_type == 3:
        format_time = data_date.strftime('%Y-%m')+'-1 00:00:00'
    if data_type == 4:
        format_time = data_date.strftime('%Y') + '-1-1 00:00:00'

    print(format_time)

    db = pymysql.connect('localhost', 'root', 'Ashin2018', "shanbay", charset='utf8')
    cursor = db.cursor()
    sql = '''select u.name,st.data_date,st.data_type,st.study_time,st.study_word,st.checkin_rate,st.integrity_rate,st.update_time from checkin_stat st, user_info u 
        where u.uid = st.uid and u.valid =1 and st.data_date='%s' and st.data_type = %d''' % (format_time, data_type)
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
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
            print("name=%s,data_date=%s,data_type=%d,study_time=%s,study_word=%d,checkin_rate=%d,integrity_rate=%d,update_time=%s" % \
                  (name, data_date, data_type, study_time, study_word, checkin_rate,integrity_rate, update_time))
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()

def get_last_monday(data_date):
    oneday = datetime.timedelta(days=1)
    while data_date.weekday() != calendar.MONDAY:
        data_date -= oneday
    return data_date

if __name__ == '__main__':
    #get_stat(datetime.date.today(),1)
    #get_stat(datetime.date.today(), 2)
    #get_stat(datetime.date.today(), 3)
    get_stat(datetime.date.today(), 4)