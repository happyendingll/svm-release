# -*- coding: utf-8 -*- 
import matplotlib as mpl 
import matplotlib.pyplot as plt  

indexNum=[]
for i in range(6,21):
	file_handle = open('/Users/cengzhiyuan/Downloads/machine_learning/machine-learning-ex6改造/ex6/weightindex.txt', 'r')
	line = file_handle.readlines()
	number = int(line[i-1])	
	indexNum.append(number) 

keyWord=[]
for i in range(0,15):
	file_handle = open('/Users/cengzhiyuan/Downloads/testdemo/svm-/关键字词汇集.txt', 'r')
	line = file_handle.readlines()
	number = indexNum[i]
	word = line[number-1][:-1]
	keyWord.append(word) 


weightNum=[]
for i in range(27,42):
	file_handle = open('/Users/cengzhiyuan/Downloads/machine_learning/machine-learning-ex6改造/ex6/weightindex.txt', 'r')
	line = file_handle.readlines()
	number = float(line[i-1][:6])	
	weightNum.append(number) 


custom_font = mpl.font_manager.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')   
num_list = weightNum 
rects = plt.barh(range(len(num_list)), num_list,color='rgb') 
plt.yticks( range(0,15),keyWord,fontproperties=custom_font) 
for rect in rects:
    w=rect.get_width()
    plt.text(w,rect.get_y()+rect.get_height()/2,'%.3f'%float(w),ha='left',va='center')
plt.title('关键字权值',fontproperties=custom_font) 
plt.xlim(0, 0.3)
plt.show() 