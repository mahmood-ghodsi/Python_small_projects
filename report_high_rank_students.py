import csv
import collections
import statistics
def calculate_averages(input_file_name, output_file_name):
    f = open('input_file_name')
    reader = csv.reader(f)
    fh = open('output_file_name', 'w')
    for row in reader:
        name = row[0]
        list_of_grades = list()
        for grades in row[1:]:
            int_grades = int(grades)
            list_of_grades.append(int_grades)
            average = statistics.mean(list_of_grades)
        fh.write(name+','+str(average)+'\n')



def calculate_sorted_averages(input_file_name, output_file_name):
    f = open('input_file_name')
    reader = csv.reader(f)
    fh = open('output_file_name', 'w')
    name_list = list()
    average_list = list()
    name_average_list = list()
    for row in reader:
        name_list.append(row[0])
        list_of_grades = list()
        for grades in row[1:]:
            int_grades = int(grades)
            list_of_grades.append(int_grades)
        average_list.append(statistics.mean(list_of_grades))
    name_average_list = list(zip(name_list, average_list))
    sorted_list = sorted(name_average_list, key = lambda average: (average[1],average[0]))
    for x,y in sorted_list:
        fh.write(x+','+str(y)+'\n')



def calculate_three_best(input_file_name, output_file_name):
    f = open('input_file_name')
    fh = open('output_file_name', 'w')
    reader = csv.reader(f)
    name_list = list()
    average_list = list()
    name_average_list = list()
    for row in reader:
        name_list.append(row[0])
        list_of_grades = list()
        for grades in row[1:]:
            int_grades = int(grades)
            list_of_grades.append(int_grades)
        average_list.append(statistics.mean(list_of_grades))
    name_average_list = list(zip(name_list, average_list))
    sorted_list = sorted(name_average_list, key = lambda average: (average[1],average[0]))
    fh.write(sorted_list[-1][0]+','+str(sorted_list[-1][1])+'\n')
    fh.write(sorted_list[-2][0]+','+str(sorted_list[-2][1])+'\n')
    fh.write(sorted_list[-3][0]+','+str(sorted_list[-3][1])+'\n')



def calculate_three_worst(input_file_name, output_file_name):
    f = open('input_file_name')
    fh = open('output_file_name', 'w')
    reader = csv.reader(f)
    name_list = list()
    average_list = list()
    name_average_list = list()
    for row in reader:
        name_list.append(row[0])
        list_of_grades = list()
        for grades in row[1:]:
            int_grades = int(grades)
            list_of_grades.append(int_grades)
        average_list.append(statistics.mean(list_of_grades))
    name_average_list = list(zip(name_list, average_list))
    sorted_list = sorted(name_average_list, key = lambda average: (average[1],average[0]))
    fh.write(str(sorted_list[0][1])+'\n')
    fh.write(str(sorted_list[1][1])+'\n')
    fh.write(str(sorted_list[2][1])+'\n')




def calculate_average_of_averages(input_file_name, output_file_name):
    f = open('input_file_name')
    fh = open('output_file_name', 'w')
    reader = csv.reader(f)
    name_list = list()
    average_list = list()
    name_average_list = list()
    for row in reader:
        name_list.append(row[0])
        list_of_grades = list()
        for grades in row[1:]:
            int_grades = int(grades)
            list_of_grades.append(int_grades)
        average_list.append(statistics.mean(list_of_grades))
    fh.write(str(statistics.mean(average_list)))



