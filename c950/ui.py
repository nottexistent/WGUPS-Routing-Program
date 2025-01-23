
import datetime

# Create UI for the deliveries
class UI:
      # Initialize UI object
      def __init__(self, trucks, packages, active=True):
            self.trucks = trucks
            self.packages = packages
            self.active = active
            self.recent_input = ''

      # Print the main menu
      def print_menu(self):
            print("\nHello and Welcome to WGUPS Delivery Tracking System")
            print("---------------------Options-----------------------")
            print("   1. View All Package Information                 ")
            print("   2. See Deliveries By Package ID                 ")
            print("   3. See Deliveries By Address ID                 ")
            print("   4. See Deliveries By Time Slot                  ")
            print("   5. See Deliveries By Truck ID                    ")
            print("   6. See All Deliveries                           ")
            print("   7. **See Delivery Status For Each Truck By Time   ")
            print("   8. See Mileage Information                      ")
            print("   9. See All Deliveries and Total Mileage         ")
            print("   10. Exit the Program                          \n")

      # Check the input given at the menu
      def check_menu(self):
            if self.recent_input == '1':
                  print('\nPrinting all package information...')
                  self.all_package_info()
            elif self.recent_input == '2':
                  self.deliveries_by_package()
            elif self.recent_input == '3':
                  self.deliveries_by_address()
            elif self.recent_input == '4':
                  self.deliveries_by_time()
            elif self.recent_input == '5':
                  self.deliveries_by_truck()
            elif self.recent_input == '6':
                  print("\nPrinting all deliveries...")
                  self.all_deliveries()
            elif self.recent_input == '7':
                  self.get_snapshot_at_time()
            elif self.recent_input == '8':
                  self.total_mileage()
            elif self.recent_input == '9':
                  self.all_deliveries_and_mileage()
            elif self.recent_input == '10':
                  print("Exiting the Progam...")
                  self.exit()
            else:
                  print("Invalid Input. Try Again")

      # Print all package info
      def all_package_info(self):
            active = True
            # Lookup each key in the hashtable and print the package value
            for key in range(1, self.packages.len()+1):
                  print((self.packages.lookup(f"{key}")).value)
            
            # Start the internal menu loop
            while active == True:
                  active = self.internal_menu()
            return
      
      # Print Package information by ID
      def deliveries_by_package(self):
            active = True
            # Lookup given package ID and print package if it is valid
            try: 
                  self.recent_input = input("\nEnter Package ID Here: ")
                  print("\n", self.packages.lookup(self.recent_input).value)
            except:
                  print("\nInvalid Input.")
            
            # Start the internal menu loop
            while active == True:
                  active = self.internal_menu()
            return
      
      # Print Package Information by Address ID
      def deliveries_by_address(self):
            active = True
            package_exists = False

            # Lookup a given Address ID and print packages associated with it if valid
            try: 
                  self.recent_input = input("\nEnter Address ID Here: ")
                  # Go through each package
                  for key in range(1, self.packages.len()+1):
                        package = self.packages.lookup(f"{key}").value
                        # If the packages address id is the same as the given print package
                        if (str(package.address.id) == self.recent_input):
                              print(package)
                              package_exists = True

                  # If the address ID given is valid, but there's no packages inform the user
                  if package_exists == False:
                        print("No Package At That Address")
            except:
                  print("\nInvalid Input.")
            
            # Start the internal menu loop
            while active == True:
                  active = self.internal_menu()
            return
      
      # Print Package Information by Time Slot
      def deliveries_by_time(self):
            active = True
            package_exists = False
            # Find all packages delivered between two times and print them if the input is valid
            try: 
                  # Get the start and end times
                  start_time_str = input("Enter the Starting Time (HH:MM:SS): ")
                  end_time_str = input("Enter the Ending Time (HH:MM:SS): ")
                  start_time = datetime.timedelta(hours=int(start_time_str.split(':')[0]), minutes=int(start_time_str.split(':')[1]), seconds=int(start_time_str.split(':')[2]))
                  end_time = datetime.timedelta(hours=int(end_time_str.split(':')[0]), minutes=int(end_time_str.split(':')[1]), seconds=int(end_time_str.split(':')[2]))
                  # Go through each package
                  for key in range(1, self.packages.len()+1):
                        package = self.packages.lookup(f"{key}").value
                        # If the package was delivered within the time slot print package
                        if (package.delivery_time > start_time and package.delivery_time < end_time):
                              print(package)
                              package_exists = True
                  # If no package was delivered during that time inform the user
                  if package_exists == False:
                        print("No Package Delivered During That Time")

            except:
                  print("\nInvalid Input.")
            
            # Start the internal menu loop
            while active == True:
                  active = self.internal_menu()
            return

      # See packages by truck
      def deliveries_by_truck(self):
            active = True
            # Get and print packages on a truck based on a given truck ID if its valid
            try: 
                  self.recent_input = input("\nEnter Truck ID Here: ")
                  truck = self.trucks[int(self.recent_input)-1]
                  truck.get_packages()
            except:
                  print("\nInvalid Input.")
            
            # Start the internal menu loop
            while active == True:
                  active = self.internal_menu()
            return
      
      # See all delivery information
      def all_deliveries(self):
            active = True
            # Print the delivery report for all trucks
            for truck in self.trucks:
                  print(f"---------------------Truck {truck.id}---------------------\n{truck.report}")

            # Start the internal menu loop
            while active == True:
                  active = self.internal_menu()
            return
      
      # See delivered packages at a specific time
      def get_snapshot_at_time(self):
            active = True
            # Find the status of all packages at a given time if the given time is valid
            try:
                  # Get the time
                  time_str = input("Enter the Time (HH:MM)(24-hour time): ")
                  time = datetime.timedelta(hours=int(time_str.split(':')[0]), minutes=int(time_str.split(':')[1]))
                  # Get status at time for each truck
                  for truck in self.trucks:
                        truck.get_status_at_time(time)
            except:
                  print("\nInvalid Input.")

            # Start internal menu loop
            while active == True:
                  active = self.internal_menu()
            return
      
      # print total mileage and individual truck mileage
      def total_mileage(self):
            active = True
            mileage = 0

            # Print each trucks mileage and get total mileage
            for truck in self.trucks:
                  print(f"Truck {truck.id} Mileage: {round(truck.mileage, 1)}")
                  mileage += truck.mileage
            print(f"Total Mileage: {mileage}")

            # Start internal menu loop
            while active == True:
                  active = self.internal_menu()
            return
      
      # Print all deliveries and mileage
      def all_deliveries_and_mileage(self):
            active = True
            mileage = 0
            # Print each trucks mileage, report, and then total mileage
            for truck in self.trucks:
                  print(f"---------------------Truck {truck.id}---------------------\n{truck.report}")
                  print(f"Truck {truck.id} Mileage: {truck.mileage}")
                  mileage += truck.mileage
            print(f"Total Mileage: {mileage}")
            
            # Start internal menu loop
            while active == True:
                  active = self.internal_menu()
            return
      
      # Start Internal Menu Loop
      def internal_menu(self):
            # Ask the user where they would like to go
            self.recent_input = input("\nWould you like to: \n1. Go Back \n2. Exit the Program\nEnter Menu Item Here: ")
            if self.recent_input == '1':
                  return False
            elif self.recent_input == '2':
                  self.active = False
                  return False
            else:
                  print("Invalid Input Try Again")
      
      # Exit UI Loop      
      def exit(self):
            self.active = False
            return
      
      # Start UI Loop
      def start(self):
            while self.active == True:
                  self.print_menu()
                  self.recent_input = input("Enter Menu Item Number: ")
                  self.check_menu()
