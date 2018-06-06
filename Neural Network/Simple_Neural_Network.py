from numpy import exp, array, random, dot
training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T
random.seed(1)
synaptic_weights = 2 * random.random((3, 1)) - 1
for iteration in range(10000):
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights)))) #use sigmoid function to normalize data
    '''
    Chúng ta sử dụng đường cong Sigmoid để tính output of the neuron.
    Nếu output là một số dương hoặc âm lớn, nó có ý nghĩa là tế bào thần kinh đã khá tự tin một cách này hay cách khác.
    Từ Hình 4, chúng ta có thể thấy nếu giá trị trục x tiến tới âm vô cùng hoặc dương vô cùng, đường cong Sigmoid có một độ dốc thấp (đồi thoải, gần như bằng phẳng).
    Nếu các tế bào thần kinh là tự tin rằng trọng số hiện tại là đúng, nó không muốn điều chỉnh nhiều. Nhân với độ dốc của đường cong Sigmoid là để đạt được điều này.
    '''
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
    '''
    Chúng ta sử dụng đường cong Sigmoid để tính output of the neuron.
    Nếu output là một số dương hoặc âm lớn, nó có ý nghĩa là tế bào thần kinh đã khá tự tin một cách này hay cách khác.
    Từ Hình 4, chúng ta có thể thấy nếu giá trị trục x tiến tới âm vô cùng hoặc dương vô cùng, đường cong Sigmoid có một độ dốc thấp (đồi thoải, gần như bằng phẳng).
    Nếu các tế bào thần kinh là tự tin rằng trọng số hiện tại là đúng, nó không muốn điều chỉnh nhiều. Nhân với độ dốc của đường cong Sigmoid là để đạt được điều này.
    '''
print (1 / (1 + exp(-(dot(array([1, 2, 0]), synaptic_weights)))))