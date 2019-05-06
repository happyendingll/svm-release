# -*- coding: utf-8 -*-
import numpy as np
import jieba,re
import getvocablist
import pandas as pd
import csv

file_handle = open('guitext.txt','r')

text = file_handle.read()
textindex = set()

seg_list = jieba.cut(text, cut_all=False)

pattern = re.compile('[a-zA-Z0-9\n，。、]+')

volist = getvocablist.getvocab()

# print (len(volist))

for item in seg_list:
	if pattern.findall(item):
		continue
	else:
		print(item)
		for i in range(0,len(volist)):
			if item == volist[i]:
				textindex.add(i+1)
				break

# print(textindex)


# a1 = np.mat(np.zeros((1,928)))
a1 = np.mat(np.zeros(shape=(1,7437),dtype=int))

for index in textindex:
	a1[0,index-1] = 1

print(np.shape(a1))
# print (a1)


df = pd.DataFrame(a1)

filename = 'guitext.csv'
df.to_csv('tempfile')

file_handle2 = open('tempfile','r')
file_handle3 = open(filename,'w')
i = 1
for row in file_handle2:
	if i == 2:
		file_handle3.write(row[2:])
	i = i+1
		





