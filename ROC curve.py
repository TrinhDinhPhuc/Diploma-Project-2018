import numpy as np
from sklearn.metrics import roc_curve, auc
n0, n1 = 20, 30
score0 = np.random.rand(n0)/2
label0 = np.zeros(n0, dtype = int)
score1  = np.random.rand(n1)/2 + .2
label1 = np.ones(n1, dtype = int)
scores = np.concatenate((score0, score1))
y_true = np.concatenate((label0, label1))
fpr, tpr, thresholds = roc_curve(y_true, scores, pos_label = 1)
print("True lables: \n{}\nScores: \n{}\nThresholds:\n{}\nFPR:\n{}\nTPR: \n{}\n".format(y_true,scores,thresholds,fpr,tpr))

'''
Một kỹ thuật đơn giản là ta thay giá trị threshold từ 0.5 xuống một số nhỏ hơn.
Chẳng hạn nếu chọn threshold = 0.3, thì mọi điểm được dự đoán có xác suất đầu ra lớn hơn 0.3
sẽ được dự đoán là thuộc lớp Positive. Nói cách khác, tỉ lệ các điểm được phân loại là Positive
sẽ tăng lên, kéo theo cả False Positive Rate và True Positive Rate cùng tăng lên (cột thứ nhất
trong ma trận tăng lên). Từ đây suy ra cả FNR và TNR đều giảm.
'''

import matplotlib.pyplot as plt
from itertools import cycle
plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='Đường cong ROC (area = %0.2f)' % auc(fpr, tpr))
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Ví dụ về đường cong Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()

