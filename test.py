import csv


class Item:
    # Class Level
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price is lower than 0"
        assert quantity >= 0, f"Quantity is lower than 0"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_revenues(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('csv.csv', 'r') as f:
            reader = csv.DictReader(f)
        items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero.
        # For i.e.: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"
        #return f"Item(self.name}, {self.price}, {self.quantity})" we replaced this command to avoid getting allways the name of the class Item.

class Phone(Item):
    all = []

    def __init__(self, name, price, quantity, broken_phones=0):
        # Call to super function to have acces to all attributes and methods
        super().__init__(
            name, price, quantity
        )
        # Run validations to received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal than 0"

        #Actions to execute
        Phone.all.append(self)


phone1 = Phone("jscPhonev10", 500, 5)
phone2 = Phone("jscPhonev20", 700, 5)
print(Item.all)
print(Phone.all)




