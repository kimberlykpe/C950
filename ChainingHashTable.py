# ChainingHashTable class
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # All buckets are assigned with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # This function will insert a new package into the hash table.
    # Insert and update package
    def insert(self, packageID, package):
        # Determine where the package will go in the bucket list.
        bucket = hash(packageID) % len(self.table)
        bucket_list = self.table[bucket]

        # Update the package if already present in the bucket.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == packageID:
                kv[1] = package
                return True

        # Else, insert the package to the end of the bucket list.
        key_value = [packageID, package]
        bucket_list.append(key_value)
        return True

    # Search for a package with matching key in the hash table.
    # If the package is found, return the package information, else return None.
    def search(self, packageID):
        # Determine where the package will go in the bucket list.
        bucket = hash(packageID) % len(self.table)
        bucket_list = self.table[bucket]

        # Search for the package in the bucket list.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == packageID:
                return kv[1]  # value
        return None

    # Removes the package with matching package ID from the hash table.
    def remove(self, packageID):
        # Determine where the package will be removed from in the bucket list.
        bucket = hash(packageID) % len(self.table)
        bucket_list = self.table[bucket]

        # If the package is there, remove the object from the list.
        for kv in bucket_list:
            # print (package ID)
            if kv[0] == packageID:
                bucket_list.remove([kv[0], kv[1]])

    # Print the data
    def print(self):
        for bucket in self.table:
            for kv in bucket:
                print(kv[0],kv[1])