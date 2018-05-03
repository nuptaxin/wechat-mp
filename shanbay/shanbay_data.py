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
    sql = '''select * from checkin_stat t
        where t.data_date = '%s' and t.data_type = %d''' % (format_time, data_type)
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            uid = row[1]
            data_type = row[2]
            data_date = row[3]
            study_time = row[4]
            study_word = row[5]
            checkin_ratio = row[6]
            update_time = row[7]
            # 打印结果
            print("id=%s,uid=%s,data_type=%d,data_date=%s,study_time=%d" % \
                  (id, uid, data_type, data_date, study_time))
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