class Item:
    def __init__(self, name):
        self.name = name
        print(f"An instance created from instance: {name}")


item1 = Item("Phone")
#item1.name = "Phone"
item1.price = 100
item1_quantity = 5

item2 = Item("Laptop")
#item2.name = "Laptop("
item2_price = 1000
item2.quantity = 3git