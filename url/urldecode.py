# -*- coding: utf-8 -*-

from urllib import unquote
import sys

"""
测试 urldecode 函数
"""

def urldecode(str):
	"""
	>>> print(urldecode("%E4%BD%A0%E5%A5%BD"))
	你好
	"""
	return unquote(str)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "你需要一个参数"
	else:
		print(urldecode(sys.argv[1]))
	
	