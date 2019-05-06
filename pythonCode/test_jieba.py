# -*- coding: utf-8 -*-
import jieba.analyse
import re

l = set()
for i in range(1,1001):	
	file_handle = open('./trainfloder/总汇取关键字/关键字文本%d.txt'%(i),'r')
	s = file_handle.read()

	
	number = 0
	for x in jieba.analyse.extract_tags(s, topK=20,withWeight=False):
	    print('%s' % (x))
	    l.add(x)
	    number = number + 1

	print ('the number is %d\n' %(number))


result = open('关键字词汇集.txt','w')

pattern1 = re.compile('[0-9]+')
pattern2 = re.compile('[a-zA-Z]+')
i = 1
for item in l:
	if pattern1.findall(item) or pattern2.findall(item):
		print (item)
		continue
	else:
		result.write(item+'\n')
		i = i +1