#coding=utf-8
import requests,json,urllib
import json
import re
import sys
import math
import P2P_register
reload(sys)
sys.setdefaultencoding('utf-8')



#在前端页面点击后执行对应的计划任务
def task(url):
    try:
        task = requests.get(url)
        #print task.text
        return task.text
    except:
        return u"请选择计划任务并点击执行按钮"

#输入借款编号和日期进行满标复审
def task_manbiao(url,borrowid,date):
    try:
        #进入运营系统进行复审
        if url == 'yipaiwang.co':
            adminname = u'陈强'
            password = 'cq123321'
        if url == 'yipaiwang.cc':
            adminname = u'陈强'
            password = 'cq123321'
        if url == 'yidai.co':
            adminname ='WD108472'
            password = 'jk123123'
        if url == 'yidaip2p.net':
            adminname = u'smilesoul'
            password = 'cq123321'
        op_login('http://op.'+url,adminname,password,borrowid)
        task_manbiao = requests.get('http://api.' + url + '/apitest/test/?borrowId=' + borrowid + '&issueDay=' + date)
        print task_manbiao.text
        return task_manbiao.text

    except:
        task_manbiao = requests.get('http://api.' + url + '/apitest/test/?borrowId=' + borrowid + '&issueDay=' + date)
        print task_manbiao.text
        return task_manbiao.text


#输入user_id进行逾期计划任务
def task_yuqi(url,user_id):
    try:
        task_yuqi1 = requests.get('http://task.'+url+'/repaylate.task.php?user_id='+user_id)
        task_yuqi2 = requests.get('http://task.'+url+'/runrepaylate.task.php?user_id='+user_id)
        #print task_yuqi.text
        return '【'+task_yuqi1.text+'】'+'【'+task_yuqi2.text+'】'
    except:
        return u"请选择计划任务并点击执行按钮"

#提现前三步
def task_tixian_1(url):
    #try:
        if url == 'yipaiwang.co':
            task_tixian_1 = requests.get('http://billtask.'+url+'/synctagsrecord.task.php')   #第一个计划任务
            task_tixian_2 = requests.get('http://billtask.'+url+'/withdrawLogs.task.php')     #第二个计划任务
            task_tixian_3 = requests.get('http://task.'+url+'/bkgold.task.php')                #第三个计划任务
        if url == 'yipaiwang.cc':
            task_tixian_1 = requests.get('http://billtask.'+url+'/synctagsrecord.task.php')   #第一个计划任务
            task_tixian_2 = requests.get('http://billtask.'+url+'/withdrawLogs.task.php')     #第二个计划任务
            task_tixian_3 = requests.get('http://task.'+url+'/bkgold.task.php')                #第三个计划任务
        if url == 'yidai.co' :
            task_tixian_1 = requests.get('http://bllincentertask.' + url + '/synctagsrecord.task.php')  # 第一个计划任务
            task_tixian_2 = requests.get('http://bllincentertask.' + url + '/withdrawLogs.task.php')  # 第二个计划任务
            task_tixian_3 = requests.get('http://task.' + url + '/bkgold.task.php')  # 第三个计划任务
        if url == 'yidaip2p.net':
            task_tixian_1 = requests.get('http://bllincentertask.' + url + '/synctagsrecord.task.php')  # 第一个计划任务
            task_tixian_2 = requests.get('http://bllincentertask.' + url + '/withdrawLogs.task.php')  # 第二个计划任务
            task_tixian_3 = requests.get('http://task.' + url + '/bkgold.task.php')  # 第三个计划任务
        first = task_tixian_1.text
        second = task_tixian_2.text
        third = task_tixian_3.text
        print first+second+third
        return '【'+first+'】'+'【'+second+'】'+'【'+third+'】'
    #except:
        #return u"请选择计划任务并点击执行按钮"

# 提现后两步
def task_tixian_2(url):
    try:
        if url == 'yipaiwang.co' :
            task_tixian_4 = requests.get('http://task.'+url+'/bkcheckcbalance.task.php')  # 第四个计划任务
            task_tixian_5 = requests.get('http://billtask.'+url+'/sendwithdraw.task.php')  # 第五个计划任务
        if url ==  'yipaiwang.cc':
            task_tixian_4 = requests.get('http://task.'+url+'/bkcheckcbalance.task.php')  # 第四个计划任务
            task_tixian_5 = requests.get('http://billtask.'+url+'/sendwithdraw.task.php')  # 第五个计划任务
        if url == 'yidai.co' :
            task_tixian_4 = requests.get('http://task.' + url + '/bkcheckcbalance.task.php')  # 第四个计划任务
            task_tixian_5 = requests.get('http://bllincentertask.' + url + '/sendwithdraw.task.php')  # 第五个计划任务
        if url == 'yidaip2p.net':
            task_tixian_4 = requests.get('http://task.' + url + '/bkcheckcbalance.task.php')  # 第四个计划任务
            task_tixian_5 = requests.get('http://bllincentertask.' + url + '/sendwithdraw.task.php')  # 第五个计划任务
        return '【'+task_tixian_4.text+'】'+'【'+task_tixian_5.text+'】'
    except:
        return u"请选择计划任务并点击执行按钮"

#提现最后一步的计划任务
def task_tixian(url,status,log_num):
    try:
        task_tixian = requests.get('http://bllincenter.'+url+'/withdraw/test/?status=' + status + '&log_num=' + log_num)
        # print task_manbiao.text
        #print task_tixian.url
        return task_tixian.text
    except:
        return u"请选择计划任务并点击执行按钮"

#登录运营系统对标进行复审
def op_login(url,adminname,password,borrowid):
    login_headers = {'Referer': url, 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                     'Upgrade-Insecure-Requests': '1', 'Content-Type': 'application/x-www-form-urlencoded',
                     'Accept-Encoding': 'gzip, deflate',
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
                     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

    userinformation = {'adminname': adminname, 'password': password, 'authCode': '123456'}
    s = requests.session()
    login = s.post(url, data=userinformation, headers=login_headers, verify=False)
    login1 = str(login)
    if u"登录成功" in login.text:
        print u'登录成功'
        #进行搜索标
        search_data = {'searchType':'borrow_nid','searchWord':borrowid}
        search = s.get(url+'/bdreverify/index/',params=search_data,cookies=login.cookies,headers=login_headers,verify=False)
        # 通过正则取出进入一审的url中的id
        examineid0 = re.findall(r'/bdreverify/subverify/\?id=(.+)', search.text)
        examineid1 = examineid0[0]
        examineid = examineid1[0:8]
        # 进入复审
        examine_data = {'id': examineid, 'borrow_nid': borrowid}
        examine = s.get(url+'/bdreverify/subverify/',params=examine_data,cookies=login.cookies,headers=login_headers,verify=False)
        examine01_post_data = {'borrow_status_temp': '16', 'remark': u'审核通过'}
        examine01_post = s.post(examine.url, data=examine01_post_data, cookies=login.cookies, headers=login_headers,verify=False)
    else:
        print u'登录失败'


#小数点2位后全部截位函数
def jiewei(num):
    num_x, num_y = str(num).split('.')
    num = float(num_x + '.' + num_y[0:2])
    return num

#计算罚息程序
def faxi(benjin,rate,today,enddate):
    try:
        import datetime
        today = datetime.datetime.strptime(today, '%Y%m%d')
        enddate = datetime.datetime.strptime(enddate, '%Y%m%d')
        time = today - enddate
        faxi = int(benjin) * float(rate) / 100 * time.days
        # 调用截位函数进行小数点两位后截位处理
        jiewei(faxi)
        print u'罚息是：'+str(jiewei(faxi))
        return u'罚息是：'+str(jiewei(faxi))
    except:
        return u'请输入正确的值！'

#计算公允价值
def gongyun(benjin,rate,today,enddate,status):
    try:
        import datetime,time
        #首先判断是否为延期，0表示未延期，1表示延期
        if status == '0':
            #today = time.strftime("%Y%m%d", time.localtime(time.time()))
            today = datetime.datetime.strptime(today, '%Y%m%d')
            enddate = datetime.datetime.strptime(enddate, '%Y%m%d')
            time = today - enddate
            day_lixi = int(benjin) * float(rate)/100/365
            gongyun = int(benjin) + float(day_lixi) * time.days
            print gongyun
            # 调用截位函数进行小数点两位后截位处理
            jiewei(gongyun)
            print u'公允价值是：'+ str(jiewei(gongyun))
            return u'公允价值是：'+ str(jiewei(gongyun))
        if status == '1':
            today = datetime.datetime.strptime(today, '%Y%m%d')
            enddate = datetime.datetime.strptime(enddate, '%Y%m%d')
            time = today - enddate
            day_lixi = int(benjin) * float(rate) / 100 / 365
            print day_lixi
            gongyun = int(benjin) + float(day_lixi) * time.days
            # 调用截位函数进行小数点两位后截位处理
            jiewei(gongyun)
            print u'公允价值是：' + str(jiewei(gongyun))
            return u'公允价值是：' + str(jiewei(gongyun))
    except:
        return u'请输入正确的值！'

#计算折让比例
def rate_zherang(faxi,gongyun,price):
    try:
        rate_zherang = (float(gongyun) + float(faxi) - float(price)) / (float(gongyun) + float(faxi)) * 100
        print rate_zherang
        # 对折让比例结果进行四舍五入
        rate_zherang = round(float(rate_zherang),2)
        print u'折让比例是：'+ str(rate_zherang)+ u'%'
        return u'折让比例是：' + str(rate_zherang) + u'%'
    except:
        return u'请输入正确的值！'

#计算承接人收益率
def shouyilv(borrow_money,borrow_month,rate,price,manbiao_date,received_money):
    try:
        import datetime, time
        p  = float(borrow_money) * float(rate) / 100 * int(borrow_month) / 365 - float(received_money) #到期应收利息
        # 调用截位函数进行小数点两位后截位处理
        p = jiewei(p)
        print u'待收收益是：' + str(p)
        a = float(borrow_money) + float(p)  #待收本息
        b = float(price) - float(borrow_money)   #承接加价
        today = time.strftime("%Y%m%d", time.localtime(time.time()))
        today = datetime.datetime.strptime(today, '%Y%m%d')
        manbiao_date = enddate = datetime.datetime.strptime(manbiao_date, '%Y%m%d')
        delta = datetime.timedelta(days=int(borrow_month))
        time = manbiao_date + delta - today
        print time.days
        shouyilv = ((float(p) - b) / float(price)) * 365 / time.days * 100
        print shouyilv
        # 对承接人收益率进行四舍五入操作
        shouyilv = round(float(shouyilv),2)
        print u'承接人收益率是：'+ str(shouyilv)+u'%'
        return u'待收收益是：' + str(jiewei(p)) + u'元' +u'，承接人收益率是：' + str(shouyilv) + u'%'+u'，ps：待收收益跟运营后台保持一致，可能会与投资人页面多1分钱'
    except:
        return u'请输入正确的值！'

#查询用户拥有优+情况
def eshareOverdue(url,phone,status):
    user_id = P2P_register.find_user_id01(url,'10',phone)
    eshareOverdue_data = {'user_id':str(user_id),'y':status}
    eshareOverdue = requests.get('http://task.'+url+'/eshareOverdue.task.php',params=eshareOverdue_data)
    return eshareOverdue.url

if __name__=='__main__':
    #task('http://www.yipaiwang.co/autotenderborrow/fortest')
    #task_manbiao('201807002623','20180404')
    #op_login('http://op.yipaiwang.co','陈强','cq123321','201807002710')
    faxi('1000','0.0009','20180809','20180806')
    gongyun('5555','15.5','20180805','20180708','0')
    rate_zherang('2.7','5072.32','5000')
    shouyilv('5000','182','10','5000','20180327','126.02')
