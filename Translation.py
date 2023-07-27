from collections import OrderedDict
number_words = input()
number_words = int(number_words)
list1 = list()
for word_seq in range(0,number_words):
    word_seq = input()
    word_list = word_seq.split()
    list1.append(word_list)
diction = OrderedDict()
for k,v,n,m in list1:
    diction[v] = k
    diction[n] = k
    diction[m] = k
#print(diction)
sentence = input()
sentence_list = sentence.split()
for word in sentence_list:
    print(diction.get(word,word), end = ' ')





