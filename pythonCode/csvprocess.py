# -*- coding: utf-8 -*-
import csv
import test_csv
with open('/Users/cengzhiyuan/Downloads/rmlt-minzhuziyou.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    l = list(test_csv.getlist())
    for row in reader:
    	for litem in l:
    		if row[2] == litem:
    			file_handle = open('民主自由%d.txt'%(144+l.index(litem)),'a')
    			file_handle.write(row[4])