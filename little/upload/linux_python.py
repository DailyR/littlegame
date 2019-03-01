#-*- coding:utf-8 -*-  
#Sample_Python.py  
#just used for 
''''' 
Created on 2015-X-XX 
 
@author: daily 
'''
#Sample


import time
import os

def main():
	'''docstring'''
	print "hello world!"
	print time.time()
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	time_str = time.strftime('%m%d%H%M%y')
	print time_str
	os.system('date 1119181423')
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	os.system('date %s' % time_str) 
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

class A_Class(object):
	def __init__(self):
		print "it is A_Class!"


if __name__ == '__main__':
	main()
	a = A_Class()
