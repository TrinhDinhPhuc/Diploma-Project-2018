from sklearn.feature_selection import VarianceThreshold
import numpy as np
X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
print("Ma trận ban đầu:\n{}\n\nMa trận sau khi transform:\n{}\n".format(X, sel.fit_transform(X)))
#ta có thể thấy VarianceThreshold đã xóa cột đầu tiên của ma trận vì variance của cột 0 < giá trị VarianceThreshold
#để kiểm chứng, ta sẽ thử xem giá trị của cột 0 và cột 1 của ma trận
def column(matrix, i):
    return [row[i] for row in matrix]
print("Giá trị của varianceThreshold là: {}".format(sel))
print("Giá trị variance của cột 0 là: {}\nGiá trị variance của cột 1 là: {}".format(np.var(column(X,0)),np.var(column(X,1))))