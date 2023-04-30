# Truck class
class Truck:
    # Initialize the Truck class with the parameters truck ID, package list, and starting time.
    # Used to find which packages are in which truck.
    # Used to track truck starting time.
    def __init__(self, truck_id, package_list, starting_time):
        self.truck_id = truck_id
        self.package_list = package_list
        self.starting_time = starting_time
        self.distance = 0

    # If the truck still has packages to deliver
    # Return the number of packages left in the package list.
    def has_packages_to_deliver(self):
        return len(self.package_list) > 0

