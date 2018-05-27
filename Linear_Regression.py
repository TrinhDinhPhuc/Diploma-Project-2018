#Trước tiên, chúng ta cần có hai thư viện numpy cho đại số tuyến tính và matplotlib cho việc vẽ hình.
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model # thư viện sklearn đã bao gồm model linear regression
import seaborn as sns
# chiều cao (cm)
X = np.array([[168,169,180,176,161,163,172,170,173,163,173,169,172,155]]).T
# cân nặng (kg)
y = np.array([[ 50 ,55 ,62, 64, 53 , 46, 65, 58, 73, 55, 74, 52, 71,80]]).T


# xây dựng X feature & reshape
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)
# tính các trọng số A,b,w
A = np.dot(Xbar.T, Xbar) #np.dot tích trong 2 ma trận
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)  #pseudo-inverse
# chuẩn bị cho fitting line
w_0 = w[0][0]
w_1 = w[1][0]

x0 = np.linspace(145,190,2) #chia ra 2 khoảng từ 145 đến 190 (vì chiều cao nằm trong khoảng đó)
y0 = w_0 + w_1*x0
y1 = w_1*172 + w_0
print("Phương trình sau khi học được là: y ={}x {}".format(w_1,w_0))
print( u'Chiều cao của Thanh Tùng là 172, cân nặng dự đoán: %.2f (kg), cân nặng thực tế là: 60 (kg)'  %(y1) )

plt.plot(X.T, y.T, 'ro')
plt.plot(x0, y0)
plt.axis([140, 190, 45, 95])
plt.xlabel('Chiều cao (cm)')
plt.ylabel('Cân nặng (kg)')
plt.show()