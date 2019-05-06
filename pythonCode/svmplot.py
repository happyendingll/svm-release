# -*- coding: utf-8 -*-  
import matplotlib as mpl
import matplotlib.pyplot as plt  
import linecache

predictNum=[]
for i in range(1,4):
	number=float(linecache.getline('/Users/cengzhiyuan/Downloads/machine_learning/machine-learning-ex6改造/ex6/predictNum.txt',4+i*5)[:4])
	predictNum.append(number) 



custom_font = mpl.font_manager.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc') 
num_list = predictNum 
themeList=['民主制度','民主监督','民主自由']
maxIndex = num_list.index(max(num_list))
plt.title('分类结果-->'+themeList[maxIndex],fontproperties=custom_font) 
plt.legend(prop =custom_font)
rects = plt.bar(range(len(num_list)), num_list,color='rgb')
plt.xticks( (0,1,2),('民主制度','民主监督','民主自由') ,fontproperties=custom_font)
plt.xlabel('主题分类',fontproperties=custom_font)
plt.ylabel('预测值',fontproperties=custom_font)
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')

plt.show() 

