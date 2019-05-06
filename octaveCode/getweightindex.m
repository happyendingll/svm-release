% load('/Users/cengzhiyuan/Downloads/machine_learning/machine-learning-ex6改造/ex6/model_all.txt')
[weight, idx] = sort(model.w, 'descend');

fprintf('\nTop predictors of spam: \n');
for i = 1:15
    fprintf(' %-15f (%f) \n', idx(i), weight(i));
end

top_idx=idx(1:15);
top_weight=weight(1:15);

save 'weightindex.txt' top_idx top_weight;