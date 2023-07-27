class daneshamooza:
    def __init__(self,name):
        self.name = name
        self.number = input()
        self.ages = input()
        self.heights = input()
        self.weights = input()
        self.ages_list = list()
        self.heights_list = list()
        self.weights_list = list()
        self.age_list = self.ages.split()
        for i in self.age_list:
            i = int(i)
            self.ages_list.append(i)
        self.height_list = self.heights.split()
        for i in self.height_list:
            i = int(i)
            self.heights_list.append(i)
        self.weight_list = self.weights.split()
        for i in self.weight_list:
            i = int(i)
            self.weights_list.append(i)
    def get_sen_average(self):
        self.sen_list_average = sum(self.ages_list)/len(self.ages_list)
        return self.sen_list_average
    def get_ghad_average(self):
        self.ghad_list_average = sum(self.heights_list)/len(self.heights_list)
        return self.ghad_list_average
    def get_vazn_average(self):
        self.vazn_list_average = sum(self.weights_list)/len(self.weights_list)
        return self.vazn_list_average
    def __lt__(self, other):
        if isinstance(other,daneshamooza):
            if self.ghad_list_average < other.ghad_list_average:
                return other.name
            elif self.ghad_list_average > other.ghad_list_average:
                return self.name
            elif self.ghad_list_average == other.ghad_list_average:
                if self.vazn_list_average > other.vazn_list_average:
                    return self.name
                elif self.vazn_list_average < other.vazn_list_average:
                    return other.name
                else:
                    return 'Same'


A = daneshamooza('A')
B = daneshamooza('B')
print(A.get_sen_average())
print(A.get_ghad_average())
print(A.get_vazn_average())
print(B.get_sen_average())
print(B.get_ghad_average())
print(B.get_vazn_average())
print(A<B)
