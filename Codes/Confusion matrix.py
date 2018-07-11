import numpy as np
def confusion_matrix(y_true,y_pred): # xây dựng hàm tính ma trận
    N= np.unique(y_true).shape[0]  #tính số lớp của ma trận
    cm = np.zeros((N,N)) #khởi tạo ma trận 0 NxN lớp
    for i in range(y_true.shape[0]): # lấy từng phần tử trong ma trận y_true
        cm[y_true[i],y_pred[i]] +=1
    return cm

y_true = np.array([0, 0, 0, 0, 1, 1, 1, 2, 2, 2])
y_pred = np.array([0, 1, 0, 2, 1, 1, 0, 2, 1, 2])
cnf_matrix = confusion_matrix(y_true, y_pred) #gọi hàm
print('Confusion matrix là :')
print(cnf_matrix)
#Độ chính xác Accuracy được tính bằng tổng các thành phần trên đường chéo chính chia cho tổng các thành phần trên ma trận
print('Độ chính xác Accuracy: {}%\n'.format(int(np.diagonal(cnf_matrix).sum()/cnf_matrix.sum()*100)))

normalized_confusion_matrix = cnf_matrix/cnf_matrix.sum(axis=1,keepdims=True)
print("Normalized confusion matrix là:\n {}".format(normalized_confusion_matrix))