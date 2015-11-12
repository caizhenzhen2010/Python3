import datetime
import xml.sax.saxutils
COPYRIGHT_TEMPLATE="Copyright(c){0}{1}.All rights reserved"
STYLESHEET_TEMPLATE=('<link rel="stylesheet" type="text/css"'
					  'media="all" href="{0}"/>\n')
HTML_TEMPLATE="""<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//E"\
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>{title}</title>
<!--{copyright}--!>
<meta name="Description" content="{description}"/>
<meta name="Keywords" content={"keywords"}/>
<meta equiv="content-type" content="text/thml;charset=utf-8"/>
{stylesheet}\
</head>
<body>
</body>
</html>
"""
def main