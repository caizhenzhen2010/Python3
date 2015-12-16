#! /usr/bin/env python
#coding=utf-8

line_one=[
          "苹果园",
          "古城路",
          "八角游乐园",
          "八宝山",
          "玉泉路",
          "五棵松",
          "万寿路",
          "公主坟",
          "军事博物馆",
          "木樨地",
          "南礼士路",
          "复兴门",
          "西单",
          "天安门西",
          "天安门东",
          "王府井",
          "东单",
          "建国门",
          "永安里",
          "国贸",
          "大望路",
          "四惠"]
line_two=[
          "积水潭",
          "鼓楼大街",
          "安定门",
          "雍和宫",
          "东直门",
          "东四十条",
          "朝阳门",
          "建国门",
          "北京站",
          "崇文门",
          "前门",
          "和平门",
          "宣武门",
          "长椿街",
          "复兴门",
          "阜成门",
          "车公庄",
          "西直门"]
lines=[line_one,line_two]
combinations_subway={"复兴门":{1,2},"建国门":{1,2}}
start=raw_input("输入起点:").strip()
end=raw_input("输入终点:").strip()
#找到起点和重点所在的线路
myline=dict()
myline.setdefault(start)
myline.setdefault(end)
if start in line_one:
    myline[start] = 1
elif start in line_two:
    myline[start]=2
if end in line_one:
    myline[end] = 1
elif end in line_two:
    myline[end]=2

for key,value in myline.iteritems():
    print key,value

if myline[start]==myline[end] == 1:
    print "请乘坐%d号线"%myline[start]
    for mystation in range(line_one.index(start),line_one.index(end)+1):
        print line_one[mystation]
        
if myline[start]==myline[end] == 2:
    print "请乘坐%d号线"%myline[start]
    for mystation in range(line_two.index(start),line_two.index(end)+1):
        print line_two[mystation]
        
if myline[start]!=myline[end]:
    for combinkey,combinvalue in combinations_subway.items():
        if combinvalue.issuperset({myline[start],myline[end]}):
            print "请乘坐%s号线"%myline[start]
            for mystation in range(line_one.index(start),line_one.index(combinkey)+1):
                print line_one[mystation]
            print "请在%s站换乘"%combinkey
            for mystation in range(line_two.index(combinkey),line_two.index(end)+1):
                print line_two[mystation]