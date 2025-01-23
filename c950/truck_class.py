# import
import datetime

# This class represents a delivery truck
class Truck:
    def __init__(self, id, start_time=datetime.timedelta(hours = 8,minutes = 0), current_time=datetime.timedelta(hours = 8,minutes = 0), speed=18, mileage=0, max_packages=16, packages=None, all_packages=None, remaining_packages=None, location=0):
        self.id = id
        self.location = location
        self.current_time = current_time
        self.speed = speed
        self.mileage = mileage
        self.max_packages = max_packages
        self.all_packages = all_packages if packages is not None else []
        self.remaining_packages = remaining_packages if packages is not None else []
        self.packages = packages if packages is not None else []
        self.report = ''
        self.start_time = start_time

    def get_packages(self):
        print("Packages That Have Been on the Truck: ")
        for package in self.all_packages:
            print(f"     {package}")

    # Load Packages onto truck
    # Complexity of O(1)
    def load_package(self, package, new_location, distances):
        # If truck is full stop loading into truck
        if len(self.packages) < self.max_packages:
            # Add package
            self.packages.append(package)
            package.status = "En Route"
            if package in self.remaining_packages:
                    self.remaining_packages.remove(package)
                
            # Update all packages and truck location
            self.current_time += datetime.timedelta(hours=float(distances[self.location][new_location]) / float(self.speed))
            self.location = new_location

    # Load given packages onto the truck using nearest neighbor algorithm
    # Complexity of O(n^2)
    def load_packages(self, start_time, distances):
        # Ready the truck
        start_state = self.all_packages
        self.current_time = start_time

        # load the packages with a nearest neighbor algorithm
        while self.all_packages != []:
            nearest_distance = float('inf')
            nearest_package = None

            # Find the closest package to current location
            for package in self.all_packages:
                # If the truck is at the package location and is not the package with the wrong address choose it
                if self.location == package.address.id and "Wrong" not in package.notes:
                    nearest_distance = 0
                    nearest_package = package
                    break
                # If the package is closer than the current nearest package pick it
                elif distances[self.location][package.address.id] < nearest_distance:
                    nearest_distance = distances[self.location][package.address.id]
                    nearest_package = package

            self.location = nearest_package.address.id
            self.all_packages.remove(nearest_package)
            self.load_package(nearest_package, nearest_package.address.id, distances)

        self.all_packages = start_state

    # Deliver a package
    # Complexity of O(1)
    def deliver_package(self, package, distance):
        # Update the mileage
        self.mileage += distance
        # Update the location
        self.location = package.address.id
        # Update the package status
        package.status = 'Delivered'
        # Calculate the delivery time
        delivery_time = self.current_time + datetime.timedelta(hours=distance / self.speed)
        # Update the package delivery time
        package.delivery_time = delivery_time
        # Add package to report
        self.report += (f"Package {package.id} delivered at {delivery_time} by {self}\n")
        # Return the delivery time to update the current time
        return delivery_time
    
    # Deliver all packages on the truck
    # Complexity of O(n)
    def deliver_all_packages(self, start_time, distances):
        # Set the current time to the start time of the delivery
        self.current_time = start_time
        self.start_time = start_time
        # Deliver all the packages
        while self.packages:
            #Set the current package being delivered
            package=self.packages.pop(0)
            # Set the distance to the package address
            distance = distances[self.location][package.address.id]
            # Deliver the package and set the current time
            self.current_time = self.deliver_package(package, distance)

        # Return to the hub
        self.return_to_hub(distances)

    # Return the truck to the hub
    # Complexity of O(1)
    def return_to_hub(self, distances):
        # Calculate the distances to return to the hub
        distance = distances[self.location][0]
        # Calculate the time to return to the hub
        time_taken = datetime.timedelta(hours=distance / self.speed)
        # Update the mileage
        self.mileage += distance
        # Update the current time
        self.current_time += time_taken
        # Update truck location
        self.location = 0

    # Update the address when the address is given for a loaded package
    # Complexity of O(n)
    def update_address(self, package_id, addresses, address_id):
        for package in self.packages:
            if int(package.id) == int(package_id):
                package.address = addresses[address_id]

    # Reset the truck to the start time
    # Complexity of O(1)
    def reset_truck(self):
        self.current_time = self.start_time
        self.location = 0
        self.mileage = 0

    # Get the status of the packages on a truck at a given time
    # Complexity of O(n)
    def get_status_at_time(self, time):
        # Print the header
        print(f"Truck {self.id} status at {time}:")
        # Get delivery status at the given time
        for package in self.all_packages:
            if package.delivery_time <= time:
                status = f'Delivered at {package.delivery_time} by {self.id}'
            elif self.start_time <= time:
                status = 'En Route'
            else:
                status = 'At the Hub'
            # Print the status
            print(f"     Package {package.id}: {package.address.address}, {package.city}, {package.state}, {package.zip_code} Deadline: {package.deadline}  |  {status}")


