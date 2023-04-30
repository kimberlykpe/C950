# Kimberly Escala
# Student ID: 001500495

import csv
import datetime

from Package import Package
from Truck import Truck
from ChainingHashTable import ChainingHashTable

# Empty list for distances.
distances = []
# Empty list for addresses.
addresses = []

# Load in Distance CSV file into program.
def loadDistance(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # Add in distance and/or addresses to either addresses = [] or distances = [].
            distances.append(row)
            addresses.append(row[0])


loadDistance('Distance.csv')

# Empty list for packages.
packages = []

# Hash table from ChainingHashTable.py
hash_table = ChainingHashTable()


# Load in Package data from CSV file into program.
def loadPackageData(fileName):
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # Add each package and input the characteristics of the file according to the object.
            packages.append(row)
            mID = int(row[0])
            mAddress = row[1]
            mCity = row[2]
            mState = row[3]
            mZip = row[4]
            mDeadline = row[5]
            mMass = row[6]
            mStatus = row[6]

            # Package object
            package = Package(mID, mAddress, mCity, mState, mZip, mDeadline, mMass, mStatus)
            hash_table.insert(mID, package)


loadPackageData('WGUPS Package File.csv')


# Calculate the distance from one address to another address.
def get_distance_between_addresses(address1, address2):
    address1_index = addresses.index(address1)
    address2_index = addresses.index(address2)
    # If address 1 is greater than address 2, you will return the distance.
    if address1_index > address2_index:
        return float(distances[address1_index][address2_index + 1])
    # If address 2 is greater than address 1, you will iterate to find another closer address.
    else:
        return float(distances[address2_index][address1_index + 1])


# Use Truck class to determine the minimum distance between the current address
# to the next closest address.
def deliver_truck(truck):
    current_location = addresses[0]
    current_time = truck.starting_time
    # If the truck still has packages to deliver
    while truck.has_packages_to_deliver():
        min_distance = 999
        min_package = None
        for package_ID in truck.package_list:
            package = hash_table.search(package_ID)
            # Compare the current address to the remaining undelivered packages in the truck.
            distance = get_distance_between_addresses(current_location, package.address)
            # The minimum distance will be selected by comparing the distances between the current location
            # to the remaining distances from the current location.
            if distance < min_distance:
                min_distance = distance
                min_package = package
        # If there is a package that needs to be delivered
        if min_package is not None:
            # Update the package time delivered.
            # Update current location, status, and current time.
            current_location = min_package.address
            current_time += datetime.timedelta(hours=min_distance / 18)
            min_package.status = "delivered"
            min_package.truck_start_time = truck.starting_time
            min_package.delivery_time = current_time
            # When truck driver finishes a package delivery, the package will be removed from the list.
            truck.distance += min_distance
            truck.package_list.remove(min_package.ID)


# Manually load in the package ID's to the 3 trucks.
# Add a start time so the truck drivers know when to start delivering packages.
truck_1 = Truck(1, [14, 15, 16, 34, 20, 21, 19, 13, 39, 24, 31, 12, 29, 30, 37], datetime.timedelta(hours=8))
deliver_truck(truck_1)
truck_2 = Truck(2, [1, 33, 7, 10, 5, 38, 3, 36, 18, 2, 8, 40, 6], datetime.timedelta(hours=9, minutes=30))
deliver_truck(truck_2)


# Update package 9 address
pkg_9 = hash_table.search(9)
pkg_9.address = "410 S State St"
pkg_9.state = "UT"
truck_3 = Truck(3, [32, 23, 11, 22, 27, 35, 17, 4, 28, 9, 25, 26], datetime.timedelta(hours=10, minutes=20))
deliver_truck(truck_3)

# For each package in the package data, the program will search using the hash table created
# in ChainingHashTable.py
for package_ID in range(1, 41):
    package = hash_table.search(package_ID)
    print(package)


# Menu screen the end user will see with a list of options to view selected data.
if __name__ == '__main__':
    print("\nWelcome to C950: Package Delivery and Information")
    # Print total milage
    print("Total milage for all trucks: ")
    print(truck_1.distance + truck_2.distance + truck_3.distance)
    # Loop until user is satisfied
    isExit = True
    while (isExit):
        print("\nPossible Menu Options:")
        print("1. Get a Single Package Status")
        print("2. Get All Package Status with a Time")
        print("3. Exit the Program")
        option = input("Chose an option (1,2, or 3): ")
        # Option 1 will print a package the end user inputs.
        if option == "1":
            package_ID = input("Enter package number: ")
            pkg = hash_table.search(int(package_ID))
            print(pkg)
        # Option 2 will print all packages with their time.
        elif option == "2":
            time_entered = input("Enter a start to check: ")
            hour,minute = time_entered.split(":")
            requested_time = datetime.timedelta(hours=int(hour),minutes=int(minute))
            for package_ID in range(1, 41):
                package = hash_table.search(package_ID)
                print(package.print_status_for_time(requested_time))
        # Option 3 will exit the program.
        elif option == "3":
            isExit = False
        # Any other number besides 1, 2, and/or 3 will print "Wrong option, try again!"
        else:
            print("Wrong option, please try again!")
