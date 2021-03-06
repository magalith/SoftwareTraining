#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import oss2
import hashlib
import random
from django.conf import settings
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


def sent_sms_with_phone(phone_number):
    ans = {}
    # client = AcsClient('LTAICNrMCIXkVv7O', 'XQGp8NBdcs7OBtgY1TrvrTpbZwPUdp', 'default')
    # 短信验证码,@maglith 友情提供
    client = AcsClient('LTAIvOKVFOootzEk', 'psEqWjHnX3B4CCxA6X1g4XiFMCz5BC', 'default')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('PhoneNumbers', str(phone_number))
    request.add_query_param('TemplateCode', "SMS_171113335")
    request.add_query_param('SignName', "实训管理系统")
    # 获取随机验证码
    code = str(get_random_number_str(6))
    request.add_query_param('TemplateParam', "{\"code\": \"%s\"}" % code)

    response = client.do_action(request)

    ans["code"] = code
    ans["data"] = str(response, encoding='utf-8')
    return ans


# 获取指定长度的随机数字字符串
def get_random_number_str(length):
    ans = ""
    while len(ans) < length:
        ans += str(int(random.random()*10000000))[:6]
    return ans[-length:]
