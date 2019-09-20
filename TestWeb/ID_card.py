#coding=utf-8
import sys
import mysql.connector
from datetime import date
from datetime import timedelta
import random, os
import requests,json,urllib
import re
from bs4 import BeautifulSoup

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

def idcard_generator():
        try:
            import time
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # 数据产生日期
            # 爬虫获取随机身份证号码
            s = requests.session()
            index = s.get('https://www.tiebazhushou.com/')
            index_soup = BeautifulSoup(index.text, 'html.parser')
            # 通过正则取出身份证号码
            id_all = index_soup.find_all('table',class_='table table-hover table-bordered')
            idcard_all = str(id_all[0])
            id = re.findall(r'<td>(.+)</td>',idcard_all)
            name = str(id[0])
            idcard = id[1]
            # 进行数据库写入
            cursor = connect.cursor()
            # SQL 插入语句
            sql = "insert into hupo.id_card(username,ID_card,modify_time) values('%s','%s','%s')" % (name, idcard, now)
            # 执行sql语句
            input = cursor.execute(sql)
            connect.commit()  # 实例提交命令
            # cursor.close()
            # connect.close()
            print u"姓名是：" + name + u"，身份证号码随机生成成功：" + idcard
            return u"姓名是：" + name + u"，身份证号码随机生成成功：" + idcard

        except:
            return u"访问次数过多，请稍后再试~~~"




def idcard():

    import time
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # 数据产生日期
    # 随机生成新的18为身份证号码
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' % (
    random.randint(10, 99), random.randint(1, 99), random.randint(1, 99), random.randint(t - 80, t - 18),
    random.randint(1, 12), random.randint(1, 28), random.randint(1, 999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]
    IDCard = '%s%s' % (x, LAST[y % 11])
    # birthday = '%s-%s-%s 00:00:00' % (IDCard[6:14][0:4], IDCard[6:14][4: 6], IDCard[6:14][6:8])
    print IDCard
    return str(IDCard)




if __name__ == '__main__':
    idcard_generator()
