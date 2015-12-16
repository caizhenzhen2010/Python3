#! /usr/bin/env python
# -*- coding=utf-8 -*-
#
  
import re
  
text = '@pythontab#pythontab'
m = re.search(r"\w+", text)
if m: 
    print m.group(1)
else:
    print 'not match'