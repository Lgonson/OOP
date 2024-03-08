item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

#print(type(item1)) # str
#print(type(item1_price)) # int
#print(type(item1_quantity)) # int
#print(type(item1_price_total)) # int


#Creation of the class
#Creating an istance = Creating an object

#Creating a class
class Item:
    def __init__(self, name, price, quantity = 0):
        #print(f'An instance created: {name}')
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self): #Methods = functions insde a class
                                           #The first argument of a class is the self argument, which refers to the object
                                           #as itself
        return self.price * self.quantity


#Creating instances of the class Item
#item1 = Item()
#item1.name = 'Phone' #each of the attributes are assigned to one instance of the class.
#item1.price= 100  #each of the attributes are assigned to one instance of the class.
#item1.quantity = 5 #each of the attributes are assigned to one instance of the class.
#print(item1.calculate_total_price(item1.price, item1_quantity))

#print(type(item1)) # str
#print(type(item1.name)) # int
#print(type(item1.price)) # int
#print(type(item1.quantity)) # int


#Creating instances of the class Item
#item2 = Item()
#item2.name = 'Computer' #each of the attributes are assigned to one instance of the class.
#item2.price= 5000  #each of the attributes are assigned to one instance of the class.
#item2.quantity = 125 #each of the attributes are assigned to one instance of the class.



#Magic Methdos: methods starting with __
#Method __init__

#print(item1.name)
#print(item2.name)
#print(item1.price)
#print(item2.price)
#print(item1.quantity)
#print(item2.quantity)




#print(item1.calculate_total_price())
#print(item2.calculate_total_price())

#Validating data types
class Item:
    def __init__(self, name: str, price: float, quantity = 0): #for quantity we have already increased a value type with 0
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal than zero"
        assert quantity >= 0, f"Price {quantity} is not greater or equal than zero"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self): #Methods = functions insde a class
                                           #The first argument of a class is the self argument, which refers to the object
                                           #as itself
        return self.price * self.quantity

#Instance Attributes
item1 = Item('Phone', 150, 5)
item2 = Item('Computer', 5000, 125)
item3 = Item('Shoes', 1500, 350)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(item3.calculate_total_price())


#Class Attributes
#Attribute, which belongs to the class itself. It's also possible to
#access this attribute form the instance aswell.