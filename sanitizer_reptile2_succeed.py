import requests
import json
import pandas as pd
import numpy as np
import csv
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

my_url = 'http://221.228.242.3:11090/api/FeiFengDataManagement/FFCityManager/GetVehicleData'
my_head = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

payload = {'Page': '1', 'Size': '500', 'dtForm': '2016/7/2 8:00:16', 'dtEnd': '2018/7/22 10:00:16'}
r = requests.post(url=my_url, headers=my_head, data=payload)
rawData = r.text
data = json.loads(rawData)

dataList = data['data']

with open('asd.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['equipmentTime', 'carCode', 'gpsValid', 'gpsLatitude', 'gpsLongitude', 'gpsSpeed',
                     'gpsDirection', 'gpsAltitude', 'oilLevel', 'oilLevelUnit'])

    for dataitem in dataList:
        writer.writerow([dataitem['equipmentTime'], dataitem['carCode'], dataitem['gpsValid'], dataitem['gpsLatitude'],
                         dataitem['gpsLongitude'], dataitem['gpsSpeed'], dataitem['gpsDirection'],
                         dataitem['gpsAltitude'], dataitem['oilLevel'], dataitem['oilLevelUnit']])


