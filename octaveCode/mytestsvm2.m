%测试一篇文章
x=load('/Users/cengzhiyuan/Downloads/testdemo/svm-/guitext.csv');
load('/Users/cengzhiyuan/Downloads/machine_learning/machine-learning-ex6改造/ex6/model_all.txt')
p0 = svmPredict1(model, x);

fprintf('\n民主相关度预测: %d\n', p0);

if (p0>=0.45)
	load('/Users/cengzhiyuan/Downloads/machine_learning/machine-learning-ex6改造/ex6/model_mzzd.txt')
	p1 = svmPredict1(model_mzzd, x);

	fprintf('\n民主制度相关度预测: %d\n', p1);

	load('/Users/cengzhiyuan/Downloads/machine_learning/machine-learning-ex6改造/ex6/model_mzjd.txt')
	p2 = svmPredict1(model_mzjd, x);

	fprintf('\n民主监督相关度预测: %d\n', p2);

	load('/Users/cengzhiyuan/Downloads/machine_learning/machine-learning-ex6改造/ex6/model_mzzy.txt')
	p3 = svmPredict1(model_mzzy, x);

	fprintf('\n民主自由相关度预测: %d\n', p3);

	save 'predictNum.txt' p0 p1 p2 p3;

else
	save 'predictNum.txt' p0

end