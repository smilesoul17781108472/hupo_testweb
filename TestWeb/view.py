#coding=utf-8
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
import sys
import os
reload(sys)
sys.setdefaultencoding("utf8")

#首页
def Yidai_Test(request):
    return render_to_response('index.html')

#随机生成银行卡号
def banid(request):
    import bankid
    return render(request, 'test_result.html', {'testmsg':bankid.bankid()})

#随机生成身份证号码
def IDcard(request):
    import ID_card
    return render(request, 'test_result.html', {'testmsg':ID_card.idcard_generator()})



