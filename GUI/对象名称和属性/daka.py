import requests
from apscheduler.schedulers.blocking import BlockingScheduler
import hashlib
import requests
#
# # 使用 md5 算法
# m = hashlib.sha512()
#
# # 要计算的源数据必须是字节串格式
# # 字符串对象需要encode转化为字节串对象
# m.update("kangkai@1314".encode())
#
# # 产生哈希值对应的bytes对象
# resultBytes = m.digest()
# # 产生哈希值的十六进制表示
# resultHex = m.hexdigest()
# print(resultHex)

def login():
    url = 'https://login.italent.cn/Account/LoginOfPMD?bsmtimestamp=1621415203404427674&BSMFrom=H5'

    header = {
        'SetCookie': 'true',
        'Content-Type': 'application/json;charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 BeisenPlatform iOS NativeApp/5.2.1'
    }

    data = {
        "Password": "LFGip/p2pjnjnHtK0wv8fGVnBQfBsVpQugHvrHke/xKqQOklMjU6JKrqGwCCWj5wrfQetLxMmSJDRe3vvnYZi6bt46gTaUPYAjaVCxSaTEx0nMyv7Yvk5sWKfxo5QURdkTpy0sHU3yULEGmbCJKH2vJU6qgEcvYx/i/LXoYdrFg=",
        "UserName": "kai.kang@rootcloud.com",
        "AppSecret": "16bd2f170d174be0aa58919568c113da"
    }

    rsp = requests.post(url, json=data, headers=header)
    print(rsp.text)

login()
# def autorecord():
#     url = 'http://vxapipad.knx.com.cn/SaveMobileAttendanceRecord'
#     data = {
#
#     }
#     header = {
#
#     }
#
#     req = requests.post(url, data=data, headers=header)
#     print(req.json())
#
#
# if __name__ == '__main__':
#     scheduler = BlockingScheduler()
#
#     scheduler.add_job(autorecord, 'cron', hour=19, minute=7, second='47')
#
#     scheduler.start()
