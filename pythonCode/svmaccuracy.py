# -*- coding: utf-8 -*- 
import matplotlib as mpl 
import matplotlib.pyplot as plt  

accuracyNum=[]
for i in range(0,5):
	file_handle = open('/Users/cengzhiyuan/Downloads/machine_learning/machine-learning-ex6改造/ex6/accuracyNum.txt', 'r')
	line = file_handle.readlines()
	number = float(line[4+i*5-1][:4])	
	accuracyNum.append(number) 

custom_font = mpl.font_manager.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')   
num_list = accuracyNum 
rects = plt.barh(range(len(num_list)), num_list,color='rgb') 
plt.yticks( (0,1,2,3,4),('总体训练集','总体测试集','民主制度','民主监督','民主自由') ,fontproperties=custom_font) 
for rect in rects:
    w=rect.get_width()
    plt.text(w,rect.get_y()+rect.get_height()/2,'%.1f%%'%float(w),ha='left',va='center')
plt.title('精确度分析',fontproperties=custom_font) 
plt.xlim(0, 112)
plt.show() 