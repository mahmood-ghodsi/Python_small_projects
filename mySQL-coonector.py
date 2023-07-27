import mysql.connector
import re
print('Connecting to the Database...')
mydb = mysql.connector.connect(host = 'localhost', user ='root', passwd = 'M1321039m!',database = 'learn')
print('Connected to the Database.')
mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE maktabkhooneh_3 (username REGEX, password VARCHAR(20))')
mydb.commit()