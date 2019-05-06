# -*- coding: utf-8 -*-
import numpy as np
import jieba,re
import getvocablist
import pandas as pd

a0 = np.mat(np.zeros(shape=(1,7437),dtype=int))

for i in range(1,503):
	file_handle = open('./trainfloder/分类取特征向量/民主相关%d.txt'%(i),'r')
	text = file_handle.read()
	textindex = set()

	seg_list = jieba.cut(text, cut_all=False)

	pattern = re.compile('[a-zA-Z0-9\n，。、]+')

	volist = getvocablist.getvocab()

	print (len(volist))

	for item in seg_list:
		if pattern.findall(item):
			continue
		else:
			print(item)
			for i in range(0,len(volist)):
				if item == volist[i]:
					textindex.add(i+1)
					break

	print(textindex)


	# a1 = np.mat(np.zeros((1,928)))
	a1 = np.mat(np.zeros(shape=(1,7437),dtype=int))

	for index in textindex:
		a1[0,index-1] = 1

	print(np.shape(a1))
	print (a1)

	a0 = np.vstack((a0,a1))

df = pd.DataFrame(a0)
df.to_csv('民主相关.csv')
