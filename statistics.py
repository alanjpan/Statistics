# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:03:05 2018

Work-in-progress program frameworks for statistics functions based on https://www.khanacademy.org/math/statistics-probability

@author: alanp
"""

a = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
b = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
c = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
d = [1, 1, 2, 3, 3, 3, 3, 4]

#mean = total / n
def mean(data):
    mean = 0
    total = 0
    n = 0
    for i in data:
        total = total + i
        n = n + 1
    mean = total / n
    print('mean: ' + str(mean))

#harmonic mean = n / (1/x)
def harmonicmean(data):
    harmonicmean = 0
    total = 0
    n = 0
    for i in data:
        total = total + 1/i
        n = n + 1
    harmonicmean = n / total
    print('harmonic mean: ' + str(harmonicmean))

#median = middle value of data
def median(data):
    mid = 0
    data.sort()
    if (len(data) % 2) == 1:
        mid = int(len(data)/2)
        median = data[mid]
    else:
        mid = int(len(data)/2)
        median = (data[mid-1] + data[mid])/2
    print('median: ' + str(median))

#mode = most x count
def mode(data):
    item = {}
    for i in data:
        if i in item:
            item[i] += 1
        else:
            item[i] = 1
    mode = 0
    count = 0
    for i in item:
        if item.get(i) > count:
            count = item.get(i)
            mode = i
    print('mode: ' + str(mode))

#variance = E[(X-u)^2]
def variance(data):
    mean = 0
    total = 0
    n = 0
    for i in data:
        total += i
        n += 1
    mean = total / n
    variance = 0
    for i in data:
        variance += (i - mean)*(i - mean)
    print('variance: ' + str(variance))

import math
#standard deviation = sqrt(variance)
def stdev(data):
    mean = 0
    total = 0
    n = 0
    for i in data:
        total += i
        n += 1
    mean = total / n
    variance = 0
    for i in data:
        variance += (i - mean)*(i - mean)
    stdev = 0
    stdev = math.sqrt(variance)
    print('stdev: ' + str(stdev))

#zscore = (x - mean) / standard deviation
def zscore(data, x):
    mean = 0
    total = 0
    n = 0
    for i in data:
        total += i
        n += 1
    mean = total / n
    variance = 0
    for i in data:
        variance += (i - mean)*(i - mean)
    stdev = 0
    stdev = math.sqrt(variance)
    zscore = 0
    zscore = (x - mean) / stdev
    print('zscore: ' + str(zscore))

#linear regression accepting points [(x0,y0), (x1,y1)]
def regression_linear(points):
    x = []
    y = []
    for i in a:
        x.append(i[0])
        y.append(i[1])

    sumxy = 0
    sumx = 0
    sumy = 0
    sumx2 = 0
    n = 0
    for i in range(len(x)):
        sumxy = sumxy + x[i] * y[i]
        sumx += x[i]
        sumy += y[i]
        sumx2 += math.pow(x[i], 2)
        n += 1
    numer = sumxy - (sumx * sumy / n)
    denom = sumx2 - (math.pow(sumx, 2) / n)
    
    b1 = round(numer / denom, 4)
    b0 = (sumy/n) - b1 * (sumx/n)

    print('b1: ' + str(b1))
    print('b0: ' + str(b0))
