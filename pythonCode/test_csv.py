# -*- coding: utf-8 -*-
import csv
with open('/Users/cengzhiyuan/Downloads/rmlt-minzhuziyou.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row['title_link'] for row in reader]

# i = 1
# for item in column:
# 	file_handle = open('./trainfloder/duzhezaixian%d.txt' %(i),'w')
# 	file_handle.write(item)
# 	i = i+1
# 	file_handle.close()
l=set()
for item in column:
	l.add(item)

def getlist():
	return l