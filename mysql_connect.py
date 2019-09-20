#coding=utf-8
import mysql.connector
import time,datetime

def mysql_connect():
    # MySQL相关设置
    mysql_host = '127.0.0.1'
    mysql_user = 'root'
    mysql_passwd = 'root'
    mysql_port = '3306'
    mysql_database = 'test'

    #连接数据库
    try:
        connect = mysql.connector.connect(host=mysql_host,user=mysql_user,password=mysql_passwd,db=mysql_database,port=mysql_port,charset="utf8")
        cursor = connect.cursor(buffered=True)
        print u"Message:连接数据库成功"
        return connect, cursor
    except:
        print u"Message:连接数据库失败"





if __name__=='__main__':
    mysql_connect()