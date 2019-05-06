# -*- coding: utf-8 -*-
import csv
with open('/Users/cengzhiyuan/Downloads/sike-redian.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    column = [row[4] for row in reader]

i = 1
for item in column:
	file_handle = open('思客热点%d.txt' %(i),'w')
	file_handle.write(item)
	i = i+1
	file_handle.close()
