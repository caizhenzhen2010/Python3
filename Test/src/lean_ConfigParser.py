#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-  

#使用ConfigParser
from ConfigParser import ConfigParser
CONFIGFILE="python.txt"

config=ConfigParser()
#读取配置文件
config.read(CONFIGFILE)

#打印初始化的问候语
#要查看的区段是’message‘
print  config.get('messages', 'greeting')

#使用配置文件的一个问题读取半径
radius=input(config.get('messages', 'question')+' ')

#打印配置文件中的结果信息
#以逗号结束，在同一行内显示
print config.get('messages', 'result_message')

#get float（）将config值转换为float类型
print config.getfloat('numbers', 'pi')*radius**2