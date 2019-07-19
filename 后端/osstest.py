# -*- coding: utf-8 -*-
import oss2

# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('LTAICNrMCIXkVv7O', 'XQGp8NBdcs7OBtgY1TrvrTpbZwPUdp')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'oss-cn-hongkong.aliyuncs.com', 'lzhcloud')

# 必须以二进制的方式打开文件，因为需要知道文件包含的字节数。
# with open('/Users/lizhenghao/Desktop/Lizhenghao/MEGA共享文件/同步图片/吴京.jpeg', 'rb') as fileobj:
#     # Seek方法用于指定从第1000个字节位置开始读写。上传时会从您指定的第1000个字节位置开始上传，直到文件结束。
#     # fileobj.seek(1000, os.SEEK_SET)
#     # Tell方法用于返回当前位置。
#     current = fileobj.tell()
#     a = bucket.put_object('吴京.jpeg', fileobj)
#     print(a)

out = bucket.put_object_from_file('TMS/123.jpeg', '/Users/lizhenghao/Desktop/Lizhenghao/MEGA共享文件/同步图片/吴京.jpeg')
print(out.resp.response.url)
