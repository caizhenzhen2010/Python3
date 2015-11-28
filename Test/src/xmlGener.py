#! /usr/bin/env/Python
#! -*- encoding: utf-8 -*-

from xml.sax import parse
import xml.sax.saxutils

xmlGener=xml.sax.saxutils.XMLGenerator(encoding='utf-8')
parse('testxml.xml',xmlGener)