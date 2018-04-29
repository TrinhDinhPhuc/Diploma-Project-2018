from sklearn.feature_selection import VarianceThreshold
X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
print("Ma trận ban đầu:\n{}\n\nMa trận sau khi transform:\n{}".format(X,sel.fit_transform(X)))
print(sel)