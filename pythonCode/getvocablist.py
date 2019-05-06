# -*- coding: utf-8 -*-

def getvocab():
	file_handle = open('关键字词汇集.txt','r')
	vocablist = []

	i = 1
	for line in file_handle.readlines():
		line = line[:-1]
		vocablist.append(line)
		i = i + 1
	return vocablist
