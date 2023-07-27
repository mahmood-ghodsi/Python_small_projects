import random
class Human:
    def __init__(self):
        self.list_of_names = list()
        self.final_list = list()
        #self.number = 8
        for i in range(22):
            self.name = input()
            self.list_of_names.append(self.name)
        for i in self.list_of_names:
            self.final_list.append(i)
class Footballist(Human):
    def teamA(self):
        self.listA = list()
        for i in range(11):
            self.names = random.choice(self.final_list)
            self.listA.append(self.names)
            self.final_list.remove(self.names)
        return self.listA
        #for i in self.listA:
            #print(i, 'A')

    def teamB(self):
        self.listB = list()
        for i in range(11):
            self.names = random.choice(self.final_list)
            self.listB.append(self.names)
            self.final_list.remove(self.names)
        return self.listB
        #for i in self.listB:
            #print(i, 'B')

teams = Footballist()
listA = list()
listB = list()
listA = teams.teamA()
listB = teams.teamB()
for i in teams.list_of_names:
    if i in listA:
        print(i, 'A')
    else:
        print(i, 'B')








