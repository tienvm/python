class Ex:
    'String doc'
    count = 0

    def __init__(self, name, intt):
        self.name = name
        self.salary = intt

    def showf(self):
        print('SHow Name {0} SHow INT{1}'.format(self.name, self.salary))


ob = Ex('tienvm', 4)
ob.showf()
print(ob.count)
print(Ex.__base__)
