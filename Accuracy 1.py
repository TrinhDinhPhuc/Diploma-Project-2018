import numpy as np #numpy để làm việc với mảng
from sklearn.naive_bayes import GaussianNB #thư viện dùng naive-bayes
from sklearn.metrics import accuracy_score #hàm accuracy_score trong sklearn

# Dữ liệu huấn luyện đầu vào
training_points = [[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]] #các điểm
training_labels = [1, 1, 1, 2, 2, 2]  # các nhãn
X = np.array(training_points) #
Y = np.array(training_labels)
# Tạo Naive Bayes classifier
clf = GaussianNB()
clf.fit(X, Y) #train model với naive bayes

# dữ liệu test
test_points = [[1, 1], [2, 2], [3, 3], [4, 3]]
test_labels = [2, 2, 2, 1]
predicts = clf.predict(test_points) #dựa vào model sau khi đã huấn luyện, dự đoán dữ liệu test
print(predicts)
# Kết quả Accuracy tính bằng tay
count = len(["ok" for idx, label in enumerate(test_labels) if label == predicts[idx]])
print ("Kết quả Accuracy được tính bằng tay là: %f" % (float(count) / len(test_labels)))

# Calculate Accuracy Rate by using accuracy_score()
print ("Kết quả Accuracy dùng hàm accuracy_score() trong sklearn là: %f" % accuracy_score(test_labels, predicts))