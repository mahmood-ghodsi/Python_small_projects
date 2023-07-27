import datetime
class Age:
    def __init__(self):
        self.birthdate = input()
    def calculate_age(self):
        x = datetime.datetime.now()
        list_birthdate = self.birthdate.split('/')
        if int(list_birthdate[0]) > int(x.year) or int(list_birthdate[1]) > 12 or int(list_birthdate[2]) > 31:
            return 'WRONG'
        else:
            self.age = int(x.year) - int(list_birthdate[0])
            return self.age

person = Age()
print(person.calculate_age())

