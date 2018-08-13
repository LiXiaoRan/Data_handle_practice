# coding=utf-8
import requests
import json
import pandas as pd
import numpy as np
import csv
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

my_url = 'http://221.228.242.3:11090/api/FeiFengDataManagement/FFCityManager/GetProjectVehicleData'
my_head = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# 增加重试连接次数
requests.adapters.DEFAULT_RETRIES = 5

count = 0

while 1:
    count += 1
    pageNum = str(count)
    payload = {'Page': pageNum, 'Size': '500', 'dtForm': '2015/1/1 0:00:16', 'dtEnd': '2018/8/13 22:00:16'}
    r = requests.post(url=my_url, headers=my_head, data=payload)
    rawData = r.text
    data = json.loads(rawData)
    dataList = data['data']
    print 'pageNum is ', pageNum
    if dataList:
        with open('ProjectVehicleData0813.csv', 'ab') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(['equipmentTime', 'carCode', 'gpsValid', 'gpsLatitude', 'gpsLongitude', 'gpsSpeed',
                             'gpsDirection', 'gpsAltitude', 'oilLevel', 'oilLevelUnit'])

            for dataitem in dataList:
                print dataitem
                writer.writerow(
                    [dataitem['equipmentTime'], dataitem['carCode'], dataitem['gpsValid'], dataitem['gpsLatitude'],
                     dataitem['gpsLongitude'], dataitem['gpsSpeed'], dataitem['gpsDirection'],
                     dataitem['gpsAltitude'], dataitem['oilLevel'], dataitem['oilLevelUnit']])

    else:
        break


