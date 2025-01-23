# Address class to hold addresses
class Address:
    # Initialized addresses
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    # Override string method for lookup
    def __str__(self):
        return f"{self.id} - {self.name} - {self.address}"