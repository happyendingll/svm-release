clear ; close all; clc

%load('spamTrain.mat');

load('/Users/cengzhiyuan/Downloads/testdemo/svm-/trainmatrix.mat');

fprintf('\nTraining Linear SVM (Spam Classification)\n')
fprintf('(this may take 1 to 2 minutes) ...\n')

C = 0.1;
model = svmTrain(x_train, y_train, C, @linearKernel);

p1 = svmPredict(model, x_train);
a1 = mean(double(p1 == y_train)) * 100;

fprintf('训练集精确度Training Accuracy: %f\n', a1);


%计算测试集精确度
load('/Users/cengzhiyuan/Downloads/testdemo/svm-/testmatrix.mat');
p2 = svmPredict(model, x_test);
a2 = mean(double(p2 == y_test)) * 100;
fprintf('测试集精确度Training Accuracy: %f\n', a2);

%民主制度预测
load('/Users/cengzhiyuan/Downloads/testdemo/svm-/mzzdyc.mat');

fprintf('\nTraining Linear SVM (Spam Classification)\n')
fprintf('(this may take 1 to 2 minutes) ...\n')

C = 0.1;
model_mzzd = svmTrain(x_mzzd, y_mzzd, C, @linearKernel);

p3 = svmPredict(model_mzzd, x_mzzd);
a3 = mean(double(p3 == y_mzzd)) * 100;

fprintf('民主制度预测精确度Training Accuracy: %f\n', a3);


%民主监督预测
load('/Users/cengzhiyuan/Downloads/testdemo/svm-/mzjdyc.mat');

fprintf('\nTraining Linear SVM (Spam Classification)\n')
fprintf('(this may take 1 to 2 minutes) ...\n')

C = 0.1;
model_mzjd = svmTrain(x_mzjd, y_mzjd, C, @linearKernel);

p4 = svmPredict(model_mzjd, x_mzjd);
a4 = mean(double(p4 == y_mzjd)) * 100;

fprintf('民主监督预测精确度Training Accuracy: %f\n', a4);

%民主自由预测
load('/Users/cengzhiyuan/Downloads/testdemo/svm-/mzzyyc.mat');

fprintf('\nTraining Linear SVM (Spam Classification)\n')
fprintf('(this may take 1 to 2 minutes) ...\n')

C = 0.1;
model_mzzy = svmTrain(x_mzzy, y_mzzy, C, @linearKernel);

p5 = svmPredict(model_mzzy, x_mzzy);
a5 = mean(double(p5 == y_mzzy)) * 100;

fprintf('民主自由预测精确度Training Accuracy: %f\n', a5);

save 'accuracyNum.txt' a1 a2 a3 a4 a5


