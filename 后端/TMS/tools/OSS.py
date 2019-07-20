#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import oss2
import hashlib
import time
from django.conf import settings


# 传入图片,返回一个云url
def upload_to_bucket(file):
    # 阿里云子账号AccessKey
    auth = oss2.Auth('LTAICNrMCIXkVv7O', 'XQGp8NBdcs7OBtgY1TrvrTpbZwPUdp')
    # Endpoint分配香港节点
    bucket = oss2.Bucket(auth, 'oss-cn-hongkong.aliyuncs.com', 'lzhcloud')

    try:
        file_ext = file.name[str(file.name).index('.'):]
    except:
        file_ext = ''

    filename = hashlib.md5(file.read()).hexdigest()
    filename = hashlib.md5(str(filename + str(time.time())).encode('UTF-8')).hexdigest() + file_ext
    # temp_file_path = os.path.join(settings.FILE_ROOT, filename)
    # with open(temp_file_path, 'wb') as temp_file:
    #     temp_file.write(file.read())
    file.file.seek(0)
    out = bucket.put_object(str("TMS/" + filename), file.file)
    # out = bucket.put_object_from_file(filename, temp_file_path)
    # print(out.resp.response.url)
    return str(out.resp.response.url)
