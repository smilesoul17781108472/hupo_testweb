#coding=utf-8
#此程序为研发人员填写每周周报
import time
import mysql_connect

#链接数据
connect = mysql_connect.mysql_connect()[0]  # connect是由connect_mysql函数返回的第一个值
cursor = connect.cursor()

def write_weekly(username,current_content,next_content,time_zones):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # 数据产生日期
    if username == '':
        return u"请填写姓名！"
    if current_content == '':
        return u"请填写本周内容！"
    if next_content == '':
        return u"请填写下周计划！"
    if time_zones == '':
        return u"请填写时间区间！"
    else:
        # 进行数据库写入
        cursor = connect.cursor()
        # SQL 插入语句
        sql = "insert into hupo.weekReport(username,current_content,next_content,time_zones,created_time) " \
              "values('%s','%s','%s','%s','%s')" % (username,current_content,next_content,time_zones,now)
        # 执行sql语句
        input = cursor.execute(sql)
        connect.commit()  # 实例提交命令
        return u"提交成功！"

def show_weekly(username,time_zones):
    #只进行姓名数据库查询
    # SQL 查询语句
    sql = "SELECT username,time_zones,current_content,next_content from hupo.weekReport WHERE username =" + username + "order by created_time limit 100"
    # 执行sql语句
    cursor.execute(sql)
    result = cursor.fetchall()
    connect.commit()  # 实例提交命令
    id = str(result[0][0])