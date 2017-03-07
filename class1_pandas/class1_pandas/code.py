#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:31:04 2017

@author: macbook
"""

import pandas as pd
from matplotlib.pyplot import *
import numpy as np
matplotlib.style.use('ggplot')
#---------------IO Tools--------------------
'''
#读写csv文件
#pd.read_csv(filepath,header,names,skiprows,encoding)
#pd.to_csv(filepath,encoding)
print len(pd.read_csv('/Users/macbook/Documents/qianchen/wiserclub/xm.csv'))
print pd.read_csv('/Users/macbook/Documents/qianchen/wiserclub/xm.csv',header=1)
print pd.read_csv('/Users/macbook/Documents/qianchen/wiserclub/xm.csv',names=['qianchen1','qianchen2'])
print len(pd.read_csv('/Users/macbook/Documents/qianchen/wiserclub/xm.csv',skiprows=10))
print pd.read_csv('/Users/macbook/Documents/qianchen/wiserclub/xm.csv',encoding='utf-8')
print pd.read_csv('/Users/macbook/Documents/qianchen/wiserclub/xm.csv',encoding='utf-8')
'''

'''
#读写xlsx文件
wen2 = pd.read_excel('/Users/macbook/Documents/qianchen/wiserclub/sq.xlsx')
print wen2
wen3 = pd.read_excel('/Users/macbook/Documents/qianchen/wiserclub/sq.xlsx',sheetname= u'非商圈')
print wen3
'''


#---------------IO Tools--------------------

#---------------Intro to basic data structures------------- 

#Series对象创建
'''
print pd.Series([1,2,3,4,5,6])
print pd.Series({'a':'1','b':'2'})

print pd.Series(np.array(np.random.randn(100)))
print pd.read_csv('/Users/macbook/Documents/qianchen/wiserclub/xm.csv')['zhuzhiaweizhi']
'''
#Series对象基本操作
'''
print pd.Series(np.array(np.random.randn(100))).mean()
print pd.Series(np.array(np.random.randn(100)))*2
print np.exp(pd.Series(np.array(np.random.randn(100))))
'''
#Series对象基本属性
'''
print pd.Series(np.array(np.random.randn(100))).drop_duplicates()
print pd.Series(np.array(np.random.randn(100))).size
'''
'''
k = pd.DataFrame({'a':pd.Series(np.array(np.random.randn(100))),
                  'b':pd.Series(np.array(np.random.randn(100)))})
print k
print k['a']
#del k['a']
#print k
k['c'] = pd.Series(np.array(np.random.randn(100)))
print k
print k.size
print k.columns
print k.T
print k.sum(axis=0)
print k.sum(axis=1)
print type(k.values)
#分类问题
wen = pd.read_csv('/Users/macbook/Documents/qianchen/wiserclub/xm.csv')
grouped = wen.groupby('chaoxiang')
print grouped.groups.keys()
cx1 = np.array(grouped.get_group('1')['unitprice'])
cx2 = np.array(grouped.get_group('2')['unitprice'])
cx3 = np.array(grouped.get_group('3')['unitprice'])
cx4 = np.array(grouped.get_group('4')['unitprice'])
cx5 = np.array(grouped.get_group('5')['unitprice'])
cx6 = np.array(grouped.get_group('6')['unitprice'])
cx7 = np.array(grouped.get_group('7')['unitprice'])
cx8 = np.array(grouped.get_group('8')['unitprice'])
cxx = []
na = grouped.groups.keys()
del na[0]
for i in range(0,len(na)):
    cxx.append(np.array(grouped.get_group(na[i])['unitprice']))
figure()
#boxplot(cxx)
#violinplot(cxx)
#hist(cxx)
'''
#---------------Intro to basic data structures------------- 

#---------------Visualization------------- 
#pd.Series(np.array(np.random.randn(1000)),
#          index=pd.date_range('1/1/2000', periods=1000)).plot()
#pd.Series(np.array(np.random.randn(1000)),
#         index=pd.date_range('1/1/2000', periods=1000)).cumsum().plot()

k = pd.DataFrame({'a':pd.Series(np.array(np.random.randn(100))),
                  'b':pd.Series(np.array(np.random.randn(100))),
                  'c':pd.Series(np.array(np.random.randn(100))),
                  'd':pd.Series(np.array(np.random.randn(100)))})
#k['a'].plot()
#k['b'].plot()
'''
wen = pd.read_csv('/Users/macbook/Documents/qianchen/wiserclub/xm.csv')
grouped = wen.groupby('chaoxiang')
print grouped.groups.keys()
cx1 = np.array(grouped.get_group('1')['unitprice'])
cx2 = np.array(grouped.get_group('2')['unitprice'])
cx3 = np.array(grouped.get_group('3')['unitprice'])
cx4 = np.array(grouped.get_group('4')['unitprice'])
cx5 = np.array(grouped.get_group('5')['unitprice'])
cx6 = np.array(grouped.get_group('6')['unitprice'])
cx7 = np.array(grouped.get_group('7')['unitprice'])
cx8 = np.array(grouped.get_group('8')['unitprice'])
cxx = []
na = grouped.groups.keys()
del na[0]
for i in range(0,len(na)):
    cxx.append(np.array(grouped.get_group(na[i])['unitprice']))
figure()
boxplot(cxx,vert=False)
#violinplot(cxx)
#hist(cxx)
'''

#scatter(k['a'],k['b'])
#hexbin(k['a'],k['b'])
wen = pd.read_csv('/Users/macbook/Documents/qianchen/wiserclub/xm.csv')
#scatter(wen['unitprice'],wen['totalprice'])
#hexbin(wen['unitprice'],wen['totalprice'].fillna(wen['totalprice'].mean()))
#hist2d(wen['unitprice'].fillna(wen['unitprice'].mean()),
#       wen['totalprice'].fillna(wen['totalprice'].mean()))
hist(wen['unitprice'].fillna(wen['unitprice'].mean()),bins=100)