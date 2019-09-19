#coding=utf-8
import mysql.connector
import time,datetime


# MySQL相关设置
mysql_host = '192.168.253.187'
mysql_user = 'ypw_co_check'
mysql_passwd = 'VKzqe45NVDi&'
mysql_port = '3306'
mysql_database = 'test'


#连接数据库
try:
    connect = mysql.connector.connect(host=mysql_host,user=mysql_user,password=mysql_passwd,db=mysql_database,port=mysql_port,charset="utf8")
    cursor = connect.cursor()
    print u"Message:连接数据库成功"
except:
    print u"Message:连接数据库失败"


def research(phone):   #通过手机号查询user_id
    #查询
    sql_borrow_nid = "select user_id from zgxt_account.edai_users_info WHERE type_id = '10' and phone = "+phone
    effect_row_borrow_nid = cursor.execute(sql_borrow_nid)
    user_id = cursor.fetchall()
    user_id = str(user_id[0][0])
    print user_id
    return str(user_id)



def researchid(borrow_numbers):  #查询ID函数
    sql_id = "select id from zgxt_account.edai_borrow WHERE borrow_numbers = " + borrow_numbers
    effect_row_id = cursor.execute(sql_id)
    id = cursor.fetchall()
    id = str(id[0][0])
    return id



#计算优+额度公式如下
def research_FrostMoney(user_id):  #查询平台兑付标总冻结金额
    lastnumber = int(user_id)%10
    lastnumber = lastnumber + 1
    sql = "select SUM(account) from zgxt_account.edai_borrow_tender_user"+str(lastnumber)+' '+"where tender_status = '0' and pay_type = '0' and owner_userid = "+user_id    #求投资冻结金额
    #print sql
    cursor.execute(sql)
    FrostMoney = cursor.fetchall()
    try:
        FrostMoney = float(FrostMoney[0][0])
        print u"平台兑付标总冻结金额是:"+str(FrostMoney)
        return FrostMoney
    except:
        print u"平台兑付标总冻结金额是:0"
        return FrostMoney==0

def research_Money(user_id):  #查询平台兑付标总待收本金
    lastnumber = int(user_id) % 10
    lastnumber = lastnumber + 1
    sql = "select SUM(recover_account_capital_wait) from zgxt_account.edai_borrow_tender_user" + str(lastnumber) + ' ' + "where tender_status = '1' and post_type !='eshare' and pay_type = '0' and status = '1' and owner_userid = " + user_id  # 求投资冻结金额
    #print sql
    cursor.execute(sql)
    Money = cursor.fetchall()
    try:
        Money = float(Money[0][0])
        print u"平台兑付标总待收本金是："+str(Money)
        return Money
    except:
        print u"平台兑付标总待收本金是：0"
        return Money==0

def change_Money(user_id):  #查询总转让中待收本息
    lastnumber = int(user_id) % 10
    lastnumber = lastnumber + 1
    sql = "select SUM(recover_account_all) from zgxt_account.edai_borrow_tender_user" + str(lastnumber) + ' ' + "where change_status = '2' and owner_userid = " + user_id  # 求投资冻结金额
    #print sql
    cursor.execute(sql)
    changge_Money = cursor.fetchall()
    try:
        changge_Money = float(changge_Money[0][0])
        print u"转让中的金额是："+str(changge_Money)
        return changge_Money
    except:
        print u"转让中的金额是：0"
        return changge_Money==0

def research_FrostMoney_jinjiaosuo(user_id):  #查询金交所兑付标且期限大于105天的冻结金额
    lastnumber = int(user_id)%10
    lastnumber = lastnumber + 1
    sql = "select SUM(account) from zgxt_account.edai_borrow_tender_user"+str(lastnumber)+' '+"where tender_status = '0' and pay_type = '1' and remain_period >= 105 and owner_userid = "+user_id    #求投资冻结金额
    #print sql
    cursor.execute(sql)
    FrostMoney_jinjiaosuo = cursor.fetchall()
    try:
        FrostMoney_jinjiaosuo = float(FrostMoney_jinjiaosuo[0][0])
        print u"金交所兑付标且期限大于105天冻结金额是:"+str(FrostMoney_jinjiaosuo)
        return FrostMoney_jinjiaosuo
    except:
        print u"金交所兑付标且期限大于105天冻结金额是:0"
        return FrostMoney_jinjiaosuo==0


def research_Money_jinjiaosuo(user_id):  #查询金交所兑付标且105天内不会结清的待收本金
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=105)
    n_days = now + delta
    time_105 = n_days.strftime('%Y-%m-%d 23:59:59')
    #print time_105
    # 转换成时间数组
    timeArray = time.strptime(time_105, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    timestamp = int(timestamp)
    lastnumber = int(user_id)%10
    lastnumber = lastnumber + 1
    sql = "select SUM(recover_account_capital_wait) from zgxt_account.edai_borrow_tender_user"+str(lastnumber)+' '+"where tender_status = '1' and pay_type = '1' and repay_last_time >="+ str(timestamp)+" and owner_userid = "+user_id    #求投资冻结金额
    #print sql
    cursor.execute(sql)
    Money_jinjiaosuo = cursor.fetchall()
    try:
        Money_jinjiaosuo = float(Money_jinjiaosuo[0][0])
        print u"金交所兑付标且105天内不会结清的待收本金是:"+str(Money_jinjiaosuo)
        return Money_jinjiaosuo
    except:
        print u"金交所兑付标且105天内不会结清的待收本金是:0"
        return Money_jinjiaosuo==0


def research_eshareMoney(user_id):  #查询优+待回购总额
    sql = "select SUM(repay_account) from zgxt_account.edai_borrow_repay where post_type = 'eshare' AND repay_status = '0' and user_id = "+user_id    #求投资冻结金额
    #print sql
    cursor.execute(sql)
    eshareMoney = cursor.fetchall()
    try:
        eshareMoney = float(eshareMoney[0][0])
        print u"优+待回购总额是:"+str(eshareMoney)
        return eshareMoney
    except:
        print u"优+待回购总额是:0"
        return eshareMoney==0

def yanqi_eshare(user_id):  #查询逾期的优+待回购总额
    sql = "select SUM(repay_account) from zgxt_account.edai_borrow_repay where post_type = 'eshare' AND status_small='17' and user_id = "+user_id    #求投资冻结金额
    #print sql
    cursor.execute(sql)
    yanqi_eshareMoney = cursor.fetchall()
    try:
        yanqi_eshareMoney = float(yanqi_eshareMoney[0][0])
        print u"逾期的优+待回购总额是:"+str(yanqi_eshareMoney)
        return yanqi_eshareMoney
    except:
        print u"逾期的优+待回购总额是:0"
        return yanqi_eshareMoney==0

def day3_eshare(user_id):  #查询今明后三天的优+待回购总额
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=2)
    n_days = now + delta
    time_105 = n_days.strftime('%Y-%m-%d 23:59:59')
    #print time_105
    # 转换成时间数组
    timeArray = time.strptime(time_105, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    timestamp = int(timestamp)
    sql = "select SUM(repay_account) from zgxt_account.edai_borrow_repay where post_type = 'eshare' AND status_small='0' AND repay_time <="+ str(timestamp)+" and user_id = "+user_id    #求投资冻结金额
    #print sql
    cursor.execute(sql)
    day3_eshareMoney = cursor.fetchall()
    try:
        day3_eshareMoney = float(day3_eshareMoney[0][0])
        print u"今明后三天的优+待回购总额是:"+str(day3_eshareMoney)
        return day3_eshareMoney
    except:
        print u"今明后三天的优+待回购总额是:0"
        return day3_eshareMoney==0

def balance(user_id):  #查询用户可用余额
    sql = "select balance from zgxt_account.edai_user_count where user_id = "+user_id    #求投资冻结金额
    #print sql
    cursor.execute(sql)
    balance_Money = cursor.fetchall()
    try:
        balance_Money = float(balance_Money[0][0])
        print u"用户可用余额是:"+str(balance_Money)
        return balance_Money
    except:
        print u"用户可用余额是:0"
        return balance_Money==0

'''connect.commit()
cursor.close()  # 关闭游标
connect.close()  # 释放数据库资源'''


if __name__=='__main__':
    '''research_FrostMoney('126168')
    research_Money('126168')
    change_Money('126168')
    research_FrostMoney_jinjiaosuo('126168')
    research_Money_jinjiaosuo('126168')
    research_eshareMoney('126168')
    '''

    eshare_Money_M = (research_FrostMoney('127032')+research_Money('127032'))*0.8+(research_FrostMoney_jinjiaosuo('127032')+research_Money_jinjiaosuo('127032'))*0.8-change_Money('127032')-research_eshareMoney('127032')
    print u"M公式优+额度是：" + str(eshare_Money_M)

    eshare_Money_N = (yanqi_eshare('127032')+day3_eshare('127032'))*1.03-balance('127032')
    print u"N公式优+额度是：" + str(eshare_Money_N)

    research('17700010001')