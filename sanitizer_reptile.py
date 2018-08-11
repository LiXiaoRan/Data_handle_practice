import requests
import json
import pandas as pd
import numpy as np

my_url = 'http://221.228.242.3:11090/api/FeiFengDataManagement/FFCityManager/GetVehicleData'
my_head = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
payload = {'Page': '1000', 'Size': '500', 'dtForm': '2016/7/2 8:00:16', 'dtEnd': '2018/7/22 10:00:16'}
r = requests.post(url=my_url, headers=my_head, data=payload)
rawData = r.text
data = json.loads(rawData)

# df = pd.DataFrame(
#     columns=['equipmentTime', 'carCode', 'gpsValid', 'gpsLatitude', 'gpsLongitude', 'gpsSpeed', 'gpsDirection',
#              'gpsAltitude', 'oilLevel', 'oilLevelUnit'])
df = pd.DataFrame()

dataList = data['data']
print data
if dataList:
    print 'true'
else:
    print 'false'

# for dataitem in dataList:
#     df1 = pd.DataFrame([dataitem['equipmentTime'], dataitem['carCode'], dataitem['gpsValid'], dataitem['gpsLatitude'],
#                         dataitem['gpsLongitude'], dataitem['gpsSpeed'], dataitem['gpsDirection'],
#                         dataitem['gpsAltitude'], dataitem['oilLevel'], dataitem['oilLevelUnit']],
#                        columns=['equipmentTime', 'carCode', 'gpsValid', 'gpsLatitude', 'gpsLongitude', 'gpsSpeed',
#                                 'gpsDirection', 'gpsAltitude', 'oilLevel', 'oilLevelUnit'])
#     df.append(df1, ignore_index=True)
#
# df.to_csv('asd.csv')


# pd.DataFrame({
#         'equipmentTime': dataitem['equipmentTime'],
#         'carCode': dataitem['carCode'],
#         'gpsValid': dataitem['gpsValid'],
#         'gpsLatitude': dataitem['gpsLatitude'],
#         'gpsLongitude': dataitem['gpsLongitude'],
#         'gpsSpeed': dataitem['gpsSpeed'],
#         'gpsDirection': dataitem['gpsDirection'],
#         'gpsAltitude': dataitem['gpsAltitude'],
#         'oilLevel': dataitem['oilLevel'],
#         'oilLevelUnit': dataitem['oilLevelUnit']
#     })
