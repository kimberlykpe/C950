# Package class
class Package:
    # Initialize Package class with the parameters of the Package CSV file.
    def __init__(self, ID, address, deadline, city, state, zip, mass, status):
        self.ID = ID
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zip = zip
        self.mass = mass
        self.status = status
        self.delivery_time = None
        self.truck_start_time = None

    # The Package class objects are defined as strings and are used as a debugging tool
    # When the members of a class need to be checked.
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.deadline, self.delivery_time, self.city, self.zip, self.mass, self.status)

    # function to show the delivery status
    def print_status_for_time(self, requested_time):
        calculated_status = "at hub"
        if requested_time > self.delivery_time:
            calculated_status = "delivered"
        elif requested_time < self.truck_start_time:
            calculated_status = "at hub"
        else:
            calculated_status = "in route"
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.deadline, self.delivery_time, self.city, self.zip, self.mass, calculated_status)
