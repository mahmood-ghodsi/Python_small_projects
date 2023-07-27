import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user ='root', passwd = 'M1321039m!',database = 'learn')
mycursor = mydb.cursor()

#mycursor.execute('CREATE TABLE maktabkhooneh_1 (name VARCHAR(50), Weight smallint UNSIGNED, Height smallint UNSIGNED)')
#mycursor.execute('INSERT INTO maktabkhooneh_1 VALUES (\'Amin\', 75, 180)')
#mycursor.execute('INSERT INTO maktabkhooneh_1 VALUES (\'Mahdi\', 90, 190)')
#mycursor.execute('INSERT INTO maktabkhooneh_1 VALUES (\'Mohammad\', 75, 175)')
#mycursor.execute('INSERT INTO maktabkhooneh_1 VALUES (\'Ahmad\', 60, 175)')
#mydb.commit()
mycursor.execute('SELECT name, Weight, Height FROM maktabkhooneh_1')
name_list = list()
weight_list = list()
height_list = list()
myresult = mycursor.fetchall()
complete_list = list()
for i in myresult:
    name_list.append(i[0])
    weight_list.append(i[1])
    height_list.append(i[2])
    complete_list.append(i)
#print(complete_list)
#print(name_list)
#print(weight_list)
#print(height_list)
sorted_complete_list = sorted(complete_list, key = lambda ghad: (-ghad[2], ghad[1]))
#print(sorted_complete_list)
for (i,j,k) in sorted_complete_list:
    print(i, k, j)


