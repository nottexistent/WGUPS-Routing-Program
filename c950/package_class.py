"""A class that defines the package object for the delivery"""
class Package:
    # Initializing method
    def __init__(self, id, address, address_name, city, state, zip_code, deadline, weight, notes="None", status='At Hub', delivery_time=None):
        self.id = id
        self.address = address
        self.address_name = address_name
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.weight = weight
        self.status = status
        self.notes = notes
        self.delivery_time = delivery_time

    # Override string method for lookup
    def __str__(self):
        return f"Package {self.id}- Address: {self.address.id}, {self.city}, {self.state} {self.zip_code} | Deadline: {self.deadline} | Weight: {self.weight} | Status: {self.status} | Delivery Time: {self.delivery_time} | Notes: {self.notes}"