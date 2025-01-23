#Import necessary classes
from package_class import Package
from address_class import Address
from hash_table import HashTable
import csv

# A class to handle data extraction from the csv's
class Reader():
    # Open and retrieve the data from the spreadsheets
    # Create a package object for each package
    # Complexity of O(n)
    def extract_package_data(self, file_name, addresses):
        # Open the given file
        with open(file_name, 'r') as file_package:
            # Create an list of packages
            packages = HashTable()
            # Create a reader with appropriate headers
            csv_reader = csv.DictReader(file_package, fieldnames=['ID', 'Address', 'City', 'State', 'Zip', 'Deadline','Weight', 'Notes'], dialect='excel')

            # Get past header data
            for n in range(8):
                    next(csv_reader)

            # Read through each row with data in the file and add a corr. package object
            for row in csv_reader:
                    id = row['ID']
                    address_name = row['Address']
                    city = row['City']
                    state = row['State']
                    zip_code = row['Zip']
                    deadline = row['Deadline']
                    weight = row['Weight']
                    notes = row['Notes']
                    for address in addresses:
                            if address_name in address.address:
                                new_address = address
                    new_package = Package(id, new_address, address_name, city, state, zip_code, deadline, weight, notes)
                    packages.insert(id, new_package)

            # Return the list of packages
            return packages

    # Create Address objects for each Address
    # Complexirty of O(n)
    def extract_address_data(self, file_name):
        counter = 0
        # Open the given file
        with open(file_name, 'r') as file_address:
            # Create a reader with appropriate headers
            csv_reader = csv.DictReader(file_address, fieldnames=['Name', 'Address'], dialect='excel')
            # Create a list of addresses
            addresses = []

            # Get past header data and poorly formatted first row
            for n in range(9):
                    next(csv_reader)

            # Manually add the first row as it is poorly formatted
            first_address = Address(counter, 'Western Governors University', '4001 South 700 East, Salt Lake City, UT 84107')
            addresses.append(first_address)
            counter += 1

            # Read through each row with data in the file and add a corr. package object
            for row in csv_reader:
                    name = row['Name'].replace("\n", "").replace("\r", "")
                    address = row['Address'].replace("\n", "").replace("\r", "")
                    new_address = Address(counter, name, address)
                    addresses.append(new_address)
                    counter += 1

        # Return the list of addresses
        return addresses

    # Get and save distances between addresses
    # Complexity of O(n^2)
    def extract_distance_data(self, file_name):
        # Open the given file
        with open(file_name, 'r') as file_distance:
            # Create a reader with appropriate headers
            csv_reader = csv.DictReader(file_distance, fieldnames=['Name', 'Address', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'], dialect='excel')
            # Create an 2D array for the distances
            distance_array = []

            # Get past header data
            for n in range(8):
                next(csv_reader)

            # Read through each row with data in the file and add to distance 2D array
            for row in csv_reader:
                distances = [row[column] for column in csv_reader.fieldnames[2:]]
                distance_array.append(distances)

        # Fix the distance array so there are no empty spots and it is a float
        for i in range(len(distance_array)):
            for j in range(len(distance_array[i])):
                if distance_array[i][j] == '':
                    distance_array[i][j] = distance_array[j][i]
                    distance_array[j][i] = float(distance_array[i][j])
                    distance_array[i][j] = float(distance_array[i][j])
                    distance_array[i][i] = 0.0

        # Return the distance array
        return distance_array