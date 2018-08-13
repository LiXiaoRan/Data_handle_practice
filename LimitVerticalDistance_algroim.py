# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：    LimitVerticalDistance
  Description :  垂距限值抽稀算法
  Author :        J_hao
  date：          2017/8/17
-------------------------------------------------
  Change Activity:
                  2017/8/17:
-------------------------------------------------
"""
from __future__ import division

from math import sqrt, pow

import pandas as pd


__author__ = 'J_hao'

THRESHOLD = 0.0009  # 阈值


def point2LineDistance(point_a, point_b, point_c):
    """
    计算点a到点b c所在直线的距离
    :param point_a:
    :param point_b:
    :param point_c:
    :return:
    """
    # 首先计算b c 所在直线的斜率和截距
    if point_b[0] == point_c[0]:
        return 9999999
    slope = (point_b[1] - point_c[1]) / (point_b[0] - point_c[0])
    intercept = point_b[1] - slope * point_b[0]

    # 计算点a到b c所在直线的距离
    distance = abs(slope * point_a[0] - point_a[1] + intercept) / sqrt(1 + pow(slope, 2))
    return distance


class LimitVerticalDistance(object):
    def __init__(self):
        self.threshold = THRESHOLD
        self.qualify_list = list()

    def diluting(self, point_list):
        """
        抽稀
        :param point_list:二维点列表
        :return:
        """
        self.qualify_list.append(point_list[0])
        check_index = 1
        while check_index < len(point_list) - 1:
            distance = point2LineDistance(point_list[check_index],
                                          self.qualify_list[-1],
                                          point_list[check_index + 1])

            if distance < self.threshold:
                check_index += 1
            else:
                self.qualify_list.append(point_list[check_index])
                check_index += 1
        return self.qualify_list


if __name__ == '__main__':
    l = LimitVerticalDistance()

    data = pd.read_csv('ProjectVehicleData2.csv')
    df = pd.DataFrame(data=data)

    var = df[['gpsLongitude', 'gpsLatitude']][df.gpsValid == 'True']
    var[['gpsLongitude', 'gpsLatitude']] = var[['gpsLongitude', 'gpsLatitude']].astype(float)

    npa = var.values
    npa = npa.tolist()

    diluting = l.diluting(npa)
    print len(diluting)
    print(diluting)