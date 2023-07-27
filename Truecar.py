import re
from bs4 import BeautifulSoup
import requests
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user ='root', passwd = 'M1321039m!',database = 'learn')
mycursor = mydb.cursor()
names = list()
miles = list()
prices = list()
page = requests.get('https://www.truecar.com/used-cars-for-sale/listings/')
soup = BeautifulSoup(page.text,'html.parser')
car_cards = soup.find_all('div',attrs={'data-test':'cardContent','class':'card-content vehicle-card-body order-3','data-qa':'CardContent'})
for card in car_cards:
     car_name = card.find('span',attrs={'class':'vehicle-header-make-model text-truncate'})
     car_miles = card.find('div', attrs={'class':'font-size-1 text-truncate', 'data-test':'vehicleMileage'})
     car_price = card.find('div',attrs={'class':'heading-3 margin-y-1 font-weight-bold','data-test':'vehicleCardPricingBlockPrice','data-qa':'Heading'})
     clean_name = car_name.text.strip()
     clean_miles = car_miles.text.strip()
     clean_price = car_price.text.strip()
     names.append(clean_name)
     miles.append(clean_miles)
     prices.append(clean_price)
final_list = list(zip(names,miles,prices))
print(final_list)
model_list = list()
#car_model = input()
#car_model = str(car_model)
for i in final_list:
    #if str(i[0]) == car_model:
     if str(i[0]) == 'Chrysler 300':
        model_list.append(i)
limited_model_list = model_list[0:20]
print(limited_model_list)
mycursor.execute('CREATE TABLE TRUECAR__DATA (Model VARCHAR(150), Number_of_miles VARCHAR(15), Price VARCHAR(15))')
for i in limited_model_list:
     model = str(i[0])
     mile = str(i[1])
     price = str(i[2])
     mycursor.execute('INSERT INTO TRUECAR__DATA(Model, Number_of_miles, Price) VALUES (%s,%s,%s)',(model,mile,price))
     mydb.commit()





