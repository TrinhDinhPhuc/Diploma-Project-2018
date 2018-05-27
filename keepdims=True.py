import numpy as np
A = np.array([[1., 2, 3, 2], [4, 3, 7, 4], [1, 4, 2, 3]])
print(np.sum(A, axis = 0, keepdims = True)) #tính tổng mỗi cột theo axis = 0
print(np.sum(A, axis = 1, keepdims = True)) #tính tổng mỗi hàng theo axis = 1