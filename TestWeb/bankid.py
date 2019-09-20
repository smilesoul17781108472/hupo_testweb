#coding=utf-8
import random
import sys
import mysql.connector
import re

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
except:
    print u"Message:连接数据库失败"

#全局设置为UTF-8
reload(sys)
sys.setdefaultencoding('utf-8')

def bankid():
    try:
        import time, datetime
        #此脚本通过程序生成银行卡号，统一为农业银行的格式
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  #数据产生日期
        time = time.strftime("%Y%m%d%S", time.localtime(time.time()))  # 银行卡号构成格式
        bankid_first = '622848'
        bank_second = time
        bank_third = '10'
        #通过3段和一个随机数相加组合成为银行卡号,保证不可能重复
        bankid = bankid_first+str(random.randint(0,9))+bank_second+bank_third
        print bankid
        # 进行数据库写入
        cursor = connect.cursor()
        # SQL 插入语句
        sql = "insert into hupo.bank_id(bankid,modify_time) values('%s','%s')" % (bankid,now)
        # 执行sql语句
        input = cursor.execute(sql)
        connect.commit()  # 实例提交命令
        # cursor.close()
        # connect.close()
        print("insert ok")
        return u"银行卡号生成成功："+bankid



    except:
        return u"访问次数过多，请稍后再试~~~"


def bank_card():
    try:
        import time, datetime
        #此脚本通过程序生成银行卡号，统一为农业银行的格式
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  #数据产生日期
        time = time.strftime("%Y%m%d%S", time.localtime(time.time()))  # 银行卡号构成格式
        bankid_first = '622848'
        bank_second = time
        bank_third = '10'
        #通过3段和一个随机数相加组合成为银行卡号,保证不可能重复
        bankid = bankid_first+str(random.randint(0,9))+bank_second+bank_third
        print bankid
        # 进行数据库写入
        cursor = connect.cursor()
        # SQL 插入语句
        sql = "insert into mysql.bank_id(bankid,modify_time) values('%s','%s')" % (bankid,now)
        # 执行sql语句
        input = cursor.execute(sql)
        connect.commit()  # 实例提交命令
        # cursor.close()
        # connect.close()
        print("insert ok")
        pattern = re.compile('.{1,4}')
        bankid = (' '.join(pattern.findall(str(bankid))))
        print bankid
        return bankid



    except:
        return u"访问次数过多，请稍后再试~~~"


if __name__ == '__main__':
    bankid()