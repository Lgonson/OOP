class Phone(Item):

    def __init__(self, name, price, quantity, broken_phones=0):
        # Call to super function to have acces to all attributes and methods
        super().__init__(
            name, price, quantity
        )
        # Run validations to received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal than 0"