from collections import OrderedDict
Genre_list = ['Adventure','Action','Comedy','Romance','Horror', 'History']
number_partic = input()
number_partic = int(number_partic)
list1 = list()
for i in range(number_partic):
    name_genres = input()
    list_name_genres = name_genres.split()
    for genre in list_name_genres[1:4]:
        list1.append(genre)
#print(list1)
dic_genres = OrderedDict()
for i in list1:
    dic_genres[i] = dic_genres.get(i,0) + 1
for i in Genre_list:
    if i not in dic_genres.keys():
        dic_genres[i] = 0
list2 = list()
for k,v in dic_genres.items():
    list2.append([k,v])
#print(list2)
sorted_list = sorted(list2, key = lambda number: (-number[1],number[0]))
for (k,v) in sorted_list:
    print(k,':',v)



