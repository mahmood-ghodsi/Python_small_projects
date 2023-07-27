number_of_inputs = 10
list_of_inputs = list()
dic1 = dict()
final_list = list()
prime_maghsoomalayh = int()
for input_numbers in range(number_of_inputs):
    input_number = input()
    input_number = int(input_number)
    list_of_inputs.append(input_number)
for number in list_of_inputs:
    n = number
    factors = list()
    i = 2
    while i * i <= n:
        if n % i != 0:
            i = i + 1
        else:
            n = n // i
            factors.append(i)
    if n > 1:
        factors.append(n)
    # print(factors)
    list5 = list()
    for i in factors:
        if i not in list5:
            list5.append(i)
    final_list.append((number, len(list5)))
sorted_list = list()
sorted_list = sorted(final_list, key = lambda adad: (adad[1], adad[0]))
#print(sorted_list)
print(sorted_list[-1][0],sorted_list[-1][1])

