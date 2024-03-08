from item import Item

class Keyboard(Item):
    pay_rate = 0.89
    def __init__(self, name, price, quantity, broken_phones=0):
        # Call to super function to have acces to all attributes and methods
        super().__init__(
            name, price, quantity
        )
