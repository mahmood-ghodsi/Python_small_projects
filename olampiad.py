number_partic = input()
number_partic = int(number_partic)
list1 = list()
for i in range(number_partic):
    data = input()
    list_data = data.split('.')
    name = list_data[1]
    name_lower = name.lower()
    name_standard = name_lower.capitalize()
    list_data[1] = name_standard
    list1.append(list_data)
sorted_list = sorted(list1, key = lambda order: (order[0],order[1]))
for k,v,i in sorted_list:
    print(k,v,i)