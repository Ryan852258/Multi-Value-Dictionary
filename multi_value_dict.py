class MultiValueDictionary:
    # constructor to initialize empty dictionary
    def __init__(self):
        self.dictionary = dict()

    # function to add new key value pair to the dictionary      
    def add(self,key,value):
        if (key not in self.dictionary):
            self.dictionary[key] = [value]   
        elif (value not in self.dictionary[key]):
            self.dictionary[key].append(value)
        else:
            raise ValueError("value already exists")

    # function to remove a key value pair to dictionary
    def remove(self,key,value):
        if (key in self.dictionary):
            try:
                self.dictionary[key].remove(value)
                # if the key no longer has any members remove the key from the dict
                if(len(self.dictionary[key]) == 0):
                    self.dictionary.pop(key)
            except(ValueError):
                raise ValueError("value does not exist")
        else:
            raise KeyError("key does not exist")

    # function to check if a key exist in the dictionary
    def key_exists(self,key):
        if (key in self.dictionary):
            return True
        else:
            return False

    # function to check if a value exist for a given key
    def value_exists(self,key,value):
        if (key in self.dictionary and value in self.dictionary[key]):
            return True
        else:
            return False

    # function to return list of keys
    def keys(self):
        return list(self.dictionary.keys())

    # function to return the set of member values associated with the key
    def members(self,key):
        if (key not in self.dictionary):
            raise KeyError("key does not exist")
        else:
            return self.dictionary[key]

    # function to return the set of all the member values in the the dictionary
    def all_members(self):
        members = list(self.dictionary.values())
        # turn the 2d list of values into a single list
        flattened_members = sum(members,[])
        return flattened_members

    # function to get all the key-value pairs in "key: value" format
    def all_items(self):
        items = []
        for key in self.dictionary.keys():
            for member in self.dictionary[key]:
                items.append("{0}: {1}".format(key,member))
        return items

    # function to remove a key and all of it's values 
    def remove_all(self,key):
        if (key in self.dictionary):
            self.dictionary.pop(key)
        else:
            raise KeyError("key does not exist")

    # function to clear the dictionary
    def clear(self):
        self.dictionary = {}