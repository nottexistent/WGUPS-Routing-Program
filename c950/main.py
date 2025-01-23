"""
Student ID: 011758894
Class: C950 - Data Structures and Algorithms II
Date: 1.19.2025
Python Ver: 3.12.8
"""
"""
Desc: This program takes an input spreadsheet (WGUPS Package File.xlsx)
      and places all of the packages into a hash table. It will then
      deliver all of the packages while meeting all listed requirements. 
      It also provides an interface to view status of packages and mileage 
      of trucks.
"""

# import necessary classes
from address_class import Address
from truck_class import Truck
from package_class import Package
from hash_table import HashTable
from csv_reader import Reader
import datetime
from ui import UI

# Extract data from the csv files
reader = Reader()
addresses = reader.extract_address_data("files/WGUPS Distance Table.csv")
distances = reader.extract_distance_data("files/WGUPS Distance Table.csv")
packages = reader.extract_package_data("files/WGUPS Package File.csv", addresses)
      

# Create lists of packages ids for the trucks
truck1_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]                  
truck2_packages = [3, 9, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]
truck3_packages = [2, 4, 5, 6, 7, 8, 10, 11, 12, 25, 28, 32, 33]

# Create Trucks
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)

# Create a list of trucks
trucks = [truck1, truck2, truck3]

# Set truck start times
truck1_start = datetime.timedelta(hours=8, minutes=0, seconds=0)
truck2_start = datetime.timedelta(hours=10, minutes=20, seconds=0)
truck3_start = datetime.timedelta(hours=9, minutes=5, seconds=0)

# Go through each package and add them to the trucks
# complexity of O(n)
for key in range(1, packages.len()+1):
      package=(packages.lookup(f"{key}")).value
      if key in truck1_packages:
            truck1.all_packages.append(package)
      elif key in truck2_packages:
            truck2.all_packages.append(package)
      elif key in truck3_packages:
            truck3.all_packages.append(package)

# Load all trucks
truck1.load_packages(truck1_start, distances)
truck2.load_packages(truck2_start, distances)
truck3.load_packages(truck3_start, distances)

# Reset all trucks to starting state
truck1.reset_truck()
truck2.reset_truck()
truck3.reset_truck()

# Deliver all packages on trucks
truck1.deliver_all_packages(truck1_start, distances)
truck3.deliver_all_packages(truck3_start, distances)
truck2.update_address(9, addresses, 19)
truck2.deliver_all_packages(min(truck1.current_time, truck3.current_time), distances)

# Reset all_packages per truck for access to history in UI
for key in range(1, packages.len()+1):
      package=(packages.lookup(f"{key}")).value
      if key in truck1_packages:
            truck1.all_packages.append(package)
      elif key in truck2_packages:
            truck2.all_packages.append(package)
      elif key in truck3_packages:
            truck3.all_packages.append(package)

# Call UI
ui = UI(trucks, packages)
ui.start()



