# -*- coding: utf-8 -*-
from tkinter import *

import tkinter.messagebox 

import os




root=Tk(className='svm文本分析器')

textfiled=Text()
textfiled.grid(row=0,column=1)

def savetofile():
	contents=textfiled.get(0.0,'end')
	file_handle=open('guitext.txt','w')
	file_handle.write(contents)

def execpython():
	os.system('python3 ./onemessageprocess.py')	

def execoctave():
	os.system('cd ~/Downloads/machine_learning/machine-learning-ex6改造/ex6 && octave mytestsvm2.m')

def execplot():
	os.system('python3 ./svmplot.py')	

def showhub():
	tkinter.messagebox.showinfo(title='分析结果',message='此文本与民主话题无关')

def judge():
	file_handle = open('/Users/cengzhiyuan/Downloads/machine_learning/machine-learning-ex6改造/ex6/predictNum.txt', 'r')
	line = file_handle.readlines()
	number = float(line[4-1][:4])

	if number < 0.45:
		showhub()
	else:
		execplot()

def drawaccuracy():
	os.system('python3 ./svmaccuracy.py')

def drawKeyword():
	os.system('python3 ./keyword.py')

def analyze():
	savetofile()
	execpython()
	execoctave()
	judge()

def clear():
	textfiled.delete(0.0,'end')

button=Button(text='分析文本',command=analyze)
button.grid(row=1,column=0)

button=Button(text='清空文本',command=clear)
button.grid(row=1,column=1)

button=Button(text='训练准确度',command=drawaccuracy)
button.grid(row=1,column=2)

button=Button(text='关键字权值',command=drawKeyword)
button.grid(row=2,column=0)

button=Button(text='退出',command=root.destroy)
button.grid(row=2,column=1)

root.mainloop()