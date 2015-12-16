#! /usr/bin/python2.7
#coding=utf-8
import re
mystring ="苹果园-古城路： 2.606公里\
古城路-八角游乐园： 1.921公里\
八角游乐园-八宝山： 1.953公里 \
八宝山-玉泉路： 1.479公里 \
玉泉路-五棵松： 1.810公里\
五棵松-万寿路： 1.778公里\
万寿路-公主坟： 1.313公里\
公主坟-军事博物馆： 1.172公里\
军事博物馆-木樨地： 1.116公里\
木樨地-南礼士路： 1.295公里\
南礼士路-复兴门： 0.420公里\
复兴门-西单： 1.591公里\
西单-天安门西： 1.216公里\
天安门西-天安门东： 0.952公里\
天安门东-王府井： 0.852公里\
王府井-东单： 0.774公里\
东单-建国门： 1.230公里\
建国门-永安里： 1.376公里\
永安里-国贸： 0.790公里\
国贸-大望路： 1.385公里\
大望路-四惠： 1.661公里\
四惠-四惠东： 1.689公里"
stationswithstations=[]
stations=[]
stationwithdom1=[]
stationwithdom2=[]
stationswithstations=mystring.split('公里')
for station in stationswithstations:
    stations.append(station.split('-')[0].strip())
#for station in stations:
#    print station
for station in stations:
    stationwithdom1.append(station.center(len(station)+2,'"'))
for station in stationwithdom1:
    print station

mystr="积水潭 鼓楼大街 安定门 雍和宫 东直门 东四十条 朝阳门 建国门 北京站 崇文门 前门 和平门 宣武门 长椿街 复兴门 阜成门 车公庄 西直门"
stations=mystr.split()
for station in stations:
    stationwithdom2.append(station.center(len(station)+2,'"'))
for station in stationwithdom2:
    print station    

