# -*- coding:utf-8 -*-

import pymssql
# 读取配置文件
import ConfigHelper

# 获取数据库连接
def GetConnection():
    return pymssql.connect(server=ConfigHelper.SqlServerHost, user=ConfigHelper.SqlServerUser, password=ConfigHelper.SqlServerPwd, database=ConfigHelper.DbName, charset='utf-8')

# 执行插入语句
def Exec(sql):
    conn = GetConnection()
    ms_cursor = conn.cursor()
    ms_cursor.execute(sql)
    ms_cursor.close()
    conn.close()

c = GetConnection()

print('c')