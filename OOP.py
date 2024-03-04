item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

print(type(item1)) # str
print(type(item1_price)) # int
print(type(item1_quantity)) # int
print(type(item1_price_total)) # int


#Creation of the class
#Creating an istance = Creating an object

#Creating a class
class Item:
    def __init__(self):
        print('I AM CREATED!')
    def calculate_total_price(self, x, y): #Methods = functions insde a class
                                           #The first argument of a class is the self argument, which refers to the object
                                           #as itself
        return x * y


#Creating instances of the class Item
item1 = Item()
item1.name = 'Phone' #each of the attributes are assigned to one instance of the class.
item1.price= 100  #each of the attributes are assigned to one instance of the class.
item1.quantity = 5 #each of the attributes are assigned to one instance of the class.
#print(item1.calculate_total_price(item1.price, item1_quantity))

#print(type(item1)) # str
#print(type(item1.name)) # int
#print(type(item1.price)) # int
#print(type(item1.quantity)) # int


#Creating instances of the class Item
item2 = Item()
item2.name = 'Computer' #each of the attributes are assigned to one instance of the class.
item2.price= 5000  #each of the attributes are assigned to one instance of the class.
item2.quantity = 125 #each of the attributes are assigned to one instance of the class.
#print(item2.calculate_total_price(item2.price, item2.quantity))


#Magic Methdos: methods starting with __
#Method __init__