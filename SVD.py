#thêm thư viện
#numpy.linalg là thư viện cho phép tính SVD
from numpy import linalg as LA
#Tạo ma trận 2x2
A = [[4,0],[3,-5]]
#Tách ra 3 ma trận U, S, V riêng biệt
U, S, V = LA.svd(A)
#Đảo ngược ma trận V bằng biến V_T
V_T=V.T

print("Kiểm tra kích thước của 3 ma trận U,S,V")
print("\n U shape= {}\n S shape= {}\n V shape= {}\n".format(U.shape,S.shape,V.shape))
print("In ra 3 ma trận U, S, V tìm được:")
print ('\n U= {0}\n\n S = {1}\n\n V={2}\n'.format(U,S,V))
print("Đây là ma trận Singular value decomposition tìm được: A = {}".format((U*S*(V_T))))
