import mysql.connector
import re
mydb = mysql.connector.connect(host = 'localhost', user ='root', passwd = 'M1321039m!',database = 'learn')
mycursor = mydb.cursor()
#mycursor.execute('CREATE TABLE maktabkhooneh_2 (username VARCHAR(100), password VARCHAR(20))')
while True:
     Username = input('Enter your Email ')
     y = re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',Username)
     if y:
         Username = str(Username)
         Password = input('Enter your password ')
         Password = str(Password)
         mycursor.execute('INSERT INTO maktabkhooneh_2(username,password) VALUES (%s,%s)',(Username,Password))
         mydb.commit()
     else:
         print('Valid form should be expression@string.string')


