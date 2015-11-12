#!/usr/bin/python2.7
# -*- Coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO,filename='mylog.log')
logging.info('Starting program')
logging.info('Trying to divide 1 by 0')
logging.info('The division successed')
logging.info('Ending program')
logging.error("Can't")