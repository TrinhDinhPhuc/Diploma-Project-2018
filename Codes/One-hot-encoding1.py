from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder   #import từ thư viện sklearn dùng LabelEncoder
from sklearn.preprocessing import OneHotEncoder  #import từ thư viện sklearn dùng OneHotEncoder
# tạo một mảng mẫu
data = ['lạnh', 'lạnh', 'ấm', 'lạnh', 'nóng', 'nóng', 'ấm', 'lạnh', 'ấm', 'nóng']
values=array(data) #chuyển sang mảng n chiều
print("Mảng ban đầu: {}".format(values))
# integer encode
label_encoder = LabelEncoder() #gán biến label_encoder cho hàm LabelEncoder() để mã hóa labels
integer_encoded = label_encoder.fit_transform(values) #thực thi mã hóa các labels
print("Mảng sau khi đã mã hóa: {}".format(integer_encoded))
# binary encode
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
print(onehot_encoded)
# invert first example
inverted = label_encoder.inverse_transform([argmax(onehot_encoded[0, :])])
print(inverted)
