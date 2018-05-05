import numpy as np

def grad_Fx(x):
    return 2*x+ 5*np.cos(x)
#F(x) Hàm này không sử dụng trong thuật toán nhưng thường được dùng để kiểm tra việc tính đạo hàm của đúng không hoặc để xem giá trị của hàm số có giảm theo mỗi vòng lặp hay không.
def cost(x):
    return x**2 + 5*np.sin(x)
def Gradient_Decent(eta, x0):
    x = [x0]
    for it in range(100):
        x_new = x[-1] - eta*grad_Fx(x[-1])
        if abs(grad_Fx(x_new)) < 1e-3: #Thuật toán dừng lại khi đạo hàm có độ lớn đủ nhỏ (0.001)
            break
        x.append(x_new)
    return (x, it)
(x1, it1) = Gradient_Decent(.1, -5) # đầu vào, learning rate = 0.1, điểm bắt đầu bằng -5
(x2, it2) = Gradient_Decent(.1,  5) # đầu vào, learning rate = 0.1, điểm bắt đầu bằng 5
print('với x1 = %f, cost = %f, hội tụ sau %d bước lặp'%(x1[-1], cost(x1[-1]), it1))
print('với x2 = %f, cost = %f, hội tụ sau %d bước lặp'%(x2[-1], cost(x2[-1]), it2))
