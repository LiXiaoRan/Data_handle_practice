import pandas as pd

# sourceData1 = pd.read_csv('../ProjectVehicleData.csv')
# sourceData2 = pd.read_csv('../VehicleData.csv')
# sourceData['id'] = 0
# sourceData.to_csv('../ProjectVehicleData.csv')


# res = pd.concat([sourceData1, sourceData2], axis=0)
# res.to_csv('../sum_data.csv')

res = pd.read_csv('../sum_data.csv')
# res.drop(['index,index2'],axis=0)
del res['index']
del res['index1']
del res['index0']
# print res.to_csv('../sum_data.csv')

DataList = []
TimeList = []

# for item in res['equipmentTime']:
#     # item.split('T')[0].replace('-', '/')
#     DataList.append(item.split('T')[0].replace('-', '/'))
#     # TimeList.append(item.split('T')[1])

# print DataList
# print TimeList

# res['equipmentTime'] = DataList
# res['datailTime'] = TimeList

res.to_csv('../sum_data.csv')
print res
