#thêm thư viện xử lý ma trận
import numpy as np
#thư viện sklearn để lấy hàm min_max_scaler
from sklearn import preprocessing
#Tạo một ma trận tên X_Train
X_train = np.array([[1.,-1.,2.],[2.,0.,0.],[0.,1.,-1.]])
#gán biến min_max_scaler từ hàm MinMaxScaler() cho khoảng [0,1]
#gán biến max_abs_scaler từ hàm MaxAbsScaler() cho khoảng [-1,1]
min_max_scaler = preprocessing.MinMaxScaler()
max_abs_scaler = preprocessing.MaxAbsScaler()
#Thực hiện chuyển đổi về khoảng [0,1] và [-1,1] bằng hàm fit_transform
X_train_minmax = min_max_scaler.fit_transform(X_train)
X_train_maxabs = max_abs_scaler.fit_transform(X_train)
#in ra màn hình ma trận sau khi scaled!
print("Ma trận ban đầu:\n{}\n\nMa trận sau khi scale:\nĐối với khoảng [0,1]:\n{}\n\n"
      "Đối với khoảng [-1,1]:\n{}".format(X_train,X_train_minmax,X_train_maxabs))