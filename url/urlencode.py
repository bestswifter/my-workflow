# -*- coding: utf-8 -*-

from urllib import quote
import sys

"""
测试 urlenocde 函数
"""

def urlencode(str):
	"""
	>>> urlencode("你好")
	'%E4%BD%A0%E5%A5%BD'
	"""
	return quote(str)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "你需要一个参数"
	else:
		print(urlencode(sys.argv[1]))
	
	