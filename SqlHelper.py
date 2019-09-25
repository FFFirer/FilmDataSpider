# -*- coding:utf-8 -*-

import pymssql
# 读取配置文件
import ConfigHelper
import LogCenter

# 获取数据库连接
def GetConnection():
    return pymssql.connect(server=ConfigHelper.SqlServerHost, user=ConfigHelper.SqlServerUser, password=ConfigHelper.SqlServerPwd, database=ConfigHelper.DbName, charset='utf8')

# 执行插入语句
def Exec(sql):
    conn = GetConnection()
    ms_cursor = conn.cursor()
    ms_cursor.execute(sql)
    conn.commit()
    ms_cursor.close()
    conn.close()

def Exec(sql, params):
    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    conn.close()
    
def Query(sql, params):
    conn = GetConnection()
    ms_cursor = conn.cursor()
    ms_cursor.execute(sql, params)
    row=ms_cursor.fetchall()
    ms_cursor.close()
    conn.close()
    return row
    