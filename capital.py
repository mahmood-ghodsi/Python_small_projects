text = input()
text = text.rstrip()
sentences_list = text.split('.')
list4 = list()
#print(sentences_list)
total_list_of_words = list()
for sentence in sentences_list:
    word_list = sentence.split()
    #print(word_list)
    for word in word_list:
        total_list_of_words.append(word)
    for words in word_list[1:]:
        first_letter = words[0]
        if first_letter.isupper():
            index = total_list_of_words.index(words)
            total_list_of_words[index] = 'checked'
            list4.append([index+1,words])
if len(list4) > 0:
   for i,j in list4:
       print(i,':',j)
else:
    print('None')

