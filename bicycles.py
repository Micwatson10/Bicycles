class Bicycle(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        
class Bikeshop(object):   
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        
class Customer(object):
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
    
customer1 = Customer("Greg", 200)
customer2 = Customer("Jeremy", 500)
customer3 = Customer("Groom", 1000)


bike2 = Bicycle("Mountain", 60, 300)       #would it be better to set up a list or dictionary so I can map bike names to bike prices?
bike3 = Bicycle("Amateur", 45, 100)
bike4 = Bicycle("Super", 50, 5000)
bike5 = Bicycle("Kiddie", 35, 150)
bike6 = Bicycle("Pro", 30, 800)
bike1 = Bicycle("Racer", 50, 199) 
mybikeshop = Bikeshop("Mike's Bikes",[bike1,bike2] ) #how to make the bikes WITHIN the bike shop
         #how to make it so that I can loop through bicycles of the bike shop

for customer in customer1, customer2, customer3:
    for bike in mybikeshop.inventory:  #CREATE ANY NAME FOR WHAT YOU WANT TO ITERATE OVER, BUT CHOOSE A GOOD NAME
        if bike.cost <= customer.funds:
            print customer.name
            print bike.name
    




#print customer1.name
#if bike1.cost < customer1.funds:      #I'd rather say "FOR bike n in bikeshop...
    #print bike1.name                  #ignore store markup for now 
#if bike2.cost < customer1.funds:
    #print bike2.name

#mybikeshop.inventory = ["Racer": 100, "Mountain": 200, "Amateur": 50, "Super": 300, "Kiddie": 25, "Pro": 500]
#print mybikeshop.inventory

        
#bike1 = Bicycle("Roughrider", 50, 100)
#print bike1.name
#print bike1.weight
#print bike1.cost
