text1 = "Phúc thích xem phim , Trâm cũng thích xem phim"
text2 = "Ngoài ra , Phúc còn thích bơi lội"
bowA = text1.split(" ") # tách từ ở văn bản 1
bowB = text2.split(" ") # tách từ ở văn bản 2
#Tạo một dictionary
word_dict = set(bowA).union(set(bowB))
wordDictA = dict.fromkeys(word_dict, 0)
wordDictB = dict.fromkeys(word_dict, 0)

#Đếm số lượng từ
for word in bowA:
    wordDictA[word]+=1
for word in bowB:
    wordDictB[word]+=1

# calculate TF
def compute_TF(word_dict, bow):
    tf_dict = {}
    bow_count = len(bow)
    for word, count in word_dict.items():
        tf_dict[word] = count / float(bow_count)
    return tf_dict


def compute_IDF(doc_list):
    import math #import thư viện math
    idf_dict = {} #tạo một dictionary rỗng
    N = len(doc_list) #gán độ dài của list cho biến N
    idf_dict = dict.fromkeys(doc_list[0].keys(), 0) #tạo dictionary lưu các keys với value = 0
    #lọc ra thành 1 list gồm các từ xuất hiện >=1 lần
    for doc in doc_list:
        for word, count in doc.items():
            if count > 0:
                idf_dict[word] += 1
    for word, count in idf_dict.items():
        idf_dict[word] = math.log(N / float(count))
    return idf_dict
print("Các từ trong 2 văn bản là:\n {}".format(word_dict))
print("Số từ xuất hiện trong văn bản 1 là:\n {}\n\nSố từ xuất hiện trong văn bản 2 là:\n {}".format(wordDictA,wordDictB))
print("\nKết quả TF:\n văn bản 1: {}\n văn bản 2: {}".format(compute_TF(wordDictA,bowA),compute_TF(wordDictB,bowB)))
print("Kết Quả IDF:\n {}".format(compute_IDF([wordDictA, wordDictB])))


def compute_TFIDF(tf_bow, idfs):
    tfidf = {}
    for word, val in tf_bow.items():
        tfidf[word] = val*idfs[word]
    return tfidf
import pandas as pd
tf_bowA = compute_TF(wordDictA, bowA)
tf_bowB = compute_TF(wordDictB, bowB)
idfs=compute_IDF([wordDictA, wordDictB])
tfidf_bowA = compute_TFIDF(tf_bowA, idfs)
tfidf_bowB = compute_TFIDF(tf_bowB, idfs)
df = pd.DataFrame([tfidf_bowA, tfidf_bowB])
print(df)