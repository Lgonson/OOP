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
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_revenues(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('instances.csv', 'r') as f:
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
        return f"{self.__class__.__name__}({self.name}, {self.__price}, {self.quantity})"

    @property
    #Property decorator = Read-only attribute
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property decorator = Read-only attributes
    def name(self):
        return self.__name


    @name.setter
    #Decorator to modify variables
    def name(self, value):
        if len(value) > 10:
            raise Exception(f"Name: {value} is too long.")
        else:
            self.__name = value
            print(f'New name {value} accepted')

