# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：    DouglasPeuker
  Description :  道格拉斯-普克抽稀算法
  Author :        liran
  date：          2018/8/12
-------------------------------------------------
  Change Activity:
                  2018/8/12: 道格拉斯-普克抽稀算法
-------------------------------------------------
"""
from __future__ import division

from math import sqrt, pow

import numpy as np
import pandas as pd

__author__ = 'liran'

# THRESHOLD = 0.0001  # 阈值
THRESHOLD = 0.02  # 阈值


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


class DouglasPeuker(object):
    def __init__(self):
        self.threshold = THRESHOLD
        self.qualify_list = list()
        self.disqualify_list = list()

    def diluting(self, point_list):
        """
        抽稀
        :param point_list:二维点列表
        :return:
        """
        if len(point_list) < 3:
            self.qualify_list.extend(point_list[::-1])
        else:
            # 找到与收尾两点连线距离最大的点
            max_distance_index, max_distance = 0, 0
            for index, point in enumerate(point_list):
                if index in [0, len(point_list) - 1]:
                    continue
                distance = point2LineDistance(point, point_list[0], point_list[-1])
                if distance > max_distance:
                    max_distance_index = index
                    max_distance = distance

            # 若最大距离小于阈值，则去掉所有中间点。 反之，则将曲线按最大距离点分割
            if max_distance < self.threshold:
                self.qualify_list.append(point_list[-1])
                self.qualify_list.append(point_list[0])
            else:
                # 将曲线按最大距离的点分割成两段
                sequence_a = point_list[:max_distance_index]
                sequence_b = point_list[max_distance_index:]

                for sequence in [sequence_a, sequence_b]:
                    if len(sequence) < 3 and sequence == sequence_b:
                        self.qualify_list.extend(sequence[::-1])
                    else:
                        self.disqualify_list.append(sequence)

    def main(self, point_list):
        print len(point_list)
        self.diluting(point_list)
        while len(self.disqualify_list) > 0:
            self.diluting(self.disqualify_list.pop())
        print self.qualify_list
        print len(self.qualify_list)


if __name__ == '__main__':
    d = DouglasPeuker()

    data = pd.read_csv('VehicleData.csv')
    df = pd.DataFrame(data=data)

    var = df[['gpsLongitude', 'gpsLatitude']][df.gpsValid == 'True']
    var[['gpsLongitude', 'gpsLatitude']] = var[['gpsLongitude', 'gpsLatitude']].astype(float)

    npa = var.values
    npa = npa.tolist()

    d.main(npa)

