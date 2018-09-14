# coding=utf-8
import numpy as np
import pandas as pd
import csv as csv

#在原本的csv文件中间把数据隔开并且添加了一个逗号

padata = pd.read_csv('file/facebook_combined.csv')
source = padata['source']
datalist = []
for item in source:
    nitem = item.split(' ')
    datalist.append([nitem[0], nitem[1]])

result = pd.DataFrame(datalist, columns=['source', 'target'])

result.to_csv('file/facebook_combined2.csv')
