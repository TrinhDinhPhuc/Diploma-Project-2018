from numpy import argmax
# khởi tạo chuỗi đầu vào
data = 'xin chào'
# định nghĩa bộ chữ cái
alphabet='aăàáâbcdđeêghiklmnoôơpqrxtuưvsy '
# mapping chuỗi sang integer
char_to_int = dict((c, i) for i, c in enumerate(alphabet))
int_to_char = dict((i, c) for i, c in enumerate(alphabet))
integer_encoded = [char_to_int[char] for char in data]
print("Giá trị encode của chữ x : {}".format(integer_encoded[0]))
# one hot encoding
onehot_encoded = list()
for value in integer_encoded:
	letter = [0 for _ in range(len(alphabet))]
	letter[value] = 1
	onehot_encoded.append(letter)
print(onehot_encoded)
# trả lại giá trị sau mã hóa, ở đây ta sẽ ví dụ ta muốn lấy chữ i ở vị trí =1 trong chuỗi "xin chào" ban đầu
inverted = int_to_char[argmax(onehot_encoded[1])]
print("Giải mã: {}".format(inverted))