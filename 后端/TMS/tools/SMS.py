#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import oss2
import hashlib
import time
from django.conf import settings
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


def sent_sms_with_phone(phone_number):
    ans = {
        "code": "ok",
    }
    client = AcsClient('LTAICNrMCIXkVv7O', 'XQGp8NBdcs7OBtgY1TrvrTpbZwPUdp', 'default')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('PhoneNumbers', int(phone_number))
    request.add_query_param('TemplateCode', "SMS_144152200")
    request.add_query_param('SignName', "智能医保")
    request.add_query_param('TemplateParam', "{\"code\": \"10086\"}")

    response = client.do_action(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))

    ans["data"] = "Success"
    return ans
