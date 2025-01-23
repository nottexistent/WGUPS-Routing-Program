# hash table item
# Referenced the Zybooks Hash Tables from the Data Structures and Algorithms I course
# https://learn.zybooks.com/zybook/WGUC949DataStructuresv4/chapter/4/section/10?content_resource_id=66714445
class HashTableItem:
    def __init__(self, item_key, value):
        self.key = item_key
        self.value = value
        self.next = None

# hash table class
class HashTable:
    # Initialize HashTable
    def __init__(self, init_size=20):
        self.table = [None] * init_size
        self.size = 0

    # Iterate through the hash table
    def __iter__(self):
        for bucket in self.table:
            item = bucket
            while item is not None:
                yield (item.key, item.value)
                item = item.next

    # Get length of hash table
    def len(self):
        return self.size

    # Insert the key/item into the hash table
    # Return False if it can't
    # Retun True if the key is updated or a new pair is made
    def insert(self, key, value):
        # Get the bucket index by hashing the key
        bindex = hash(key) % len(self.table)

        # Set the item
        item = self.table[bindex]

        # Set the previous item
        previous = None

        # Search the bucket for the key
        while item is not None:
            if key == item.key:
                # Set the item
                item.value = value
                # Update the size
                self.size += 1
                return True
            
            #Set the previous item
            previous = item
            # Iterate to the next item
            item = item.next

        # The key is not found, append to the list
        if self.table[bindex] == None:
            self.table[bindex] = HashTableItem(key, value)
        else:
            previous.next = HashTableItem(key, value)
        # Update the size
        self.size += 1
        return True

    def remove(self, key):
        # Get the bucket index by hashing the key
        bindex = hash(key) % len(self.table)

        # Set the item
        item = self.table[bindex]

        # Set the previous item
        previous = None

        # Search the bucket for the key
        while item != None:
            if key == item.key:
                if previous == None:
                    # Remove list first item
                    self.table[bindex] = item.next
                else:
                    previous.next = item.next
                self.size -= 1
                return True
            
            #Set the previous item
            previous = item
            # Iterate to the next item
            item = item.next

        # Key is not found
        return False

    # Lookup an item
    def lookup(self, key):
        # Get the bucket index by hashing the key
        bindex = hash(key) % len(self.table)

        # Set the item
        item = self.table[bindex]

        # Search the bucket for the key
        while item != None:
            if key == item.key:
                # Return the corr. item found
                return item
            # Iterate to the next item
            item = item.next
        # Item was not found
        return None