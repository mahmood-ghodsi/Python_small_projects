import re
from bs4 import BeautifulSoup
import requests
import mysql.connector
from sklearn import tree
import numpy as np
mydb = mysql.connector.connect(host = 'localhost', user ='root', passwd = 'MYSQL1321039mysql!',database = 'learn')
mycursor = mydb.cursor()
list_ads = list()
for i in range(1,5):
    webpage = requests.get('https://ihome.ir/sell-residential-apartment/th-tehran?locations=iran.th.tehran&property_type=residential-apartment&paginate=30&page='+str(i)+'&is_sale=1&source=website')
    soup = BeautifulSoup(webpage.text,'html.parser')
    ad = soup.find_all('div', attrs={'data-v-47515678':"", 'class':'d-flex flex-column h-100 justify-content-between'})
    for eachad in ad:
        properties = eachad.find_all('div',attrs={'data-v-f77822e8':'', 'data-v-47515678':'', 'class':'property-detail__icons-item card-icon'})
        size_comp_text = properties[0]
        size = size_comp_text.find('span',attrs={'data-v-f77822e8':'','class':'property-detail__icons-item__value'})
        size_text = size.text.strip()
        year_comp_text = properties[1]
        year = year_comp_text.find('span',attrs={'data-v-f77822e8':'','class':'property-detail__icons-item__value'})
        year_text = re.sub(r'\s+',' ',year.text).strip()
        if year_text == 'نوساز':
            year_text = '0'
        rooms_comp_text = properties[2]
        rooms = rooms_comp_text.find('span',attrs={'data-v-f77822e8':'','class':'property-detail__icons-item__value'})
        room_text = rooms.text.strip()
        price_comp_text = eachad.find('div',attrs={'data-v-47515678':'','itemprop':'offers','itemscope':'itemscope','itemtype':'http://schema.org/Offer','class':'d-none'})
        price = price_comp_text.find('span',attrs={'data-v-47515678':'','itemprop':'price'})
        price_text = price.text.strip()
        location = eachad.find('span',attrs={'class':'sub-title','data-v-47515678':''})
        location_text = re.sub(r'\s+',' ',location.text).strip()
        list_words_location = location_text.split()
        if 'خیابان' in list_words_location:
            list_words_location.remove('خیابان')
            glue = ' '
            location_text = glue.join(list_words_location)
        list_ads.append((location_text,size_text,year_text,room_text,price_text))
#print(list_ads)
mycursor.execute('CREATE TABLE ihome_data (Location VARCHAR (100), Size VARCHAR(50), Age VARCHAR(50), Number_of_rooms VARCHAR(10), Price VARCHAR (50))')

mycursor.execute('SELECT * FROM ihome_data')
myresults = mycursor.fetchall()

#avoid redundancy
for i in list_ads:
    if i not in myresults:
        mycursor.execute('INSERT INTO ihome_data (Location, Size, Age, Number_of_rooms, Price) VALUES (%s,%s,%s,%s,%s)',(str(i[0]),str(i[1]),str(i[2]),str(i[3]),int(i[4])))
        mydb.commit()
    else:
        continue
x = []
y = []
for i in myresults:
    x.append(i[1:4])
    y.append(int(i[4]))
#print(x[0:6])
#print(y[0:6])

clf = tree.DecisionTreeRegressor()
clf = clf.fit(x, y)
new_data = [(90,0,2)]
answer = clf.predict(new_data)
print(answer)

#My program does not work when I include the location, it only predicts based on the size, number of the rooms, and age.
