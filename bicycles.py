class Bicycle(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        
        
bike1 = Bicycle("Roughrider", 50, 100)
print bike1.name
print bike1.weight
print bike1.cost
