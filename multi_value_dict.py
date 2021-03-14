class MultiValueDictionary:

    #constructor to initalize empty dictionary
    def __init__(self):
        self.dictionary = dict()

    # function to add new key value pair to the dictionary      
    def add(self,key,value):
        if (key not in self.dictionary):
            self.dictionary[key] = [value]   
        elif (value not in self.dictionary[key]):
            self.dictionary[key].append(value)
        else:
            raise ValueError("Value already exists")

    # function to remove a key value pair to dictionary
    def remove(self,key,value):
        if (key in self.dictionary):
            try:
                self.dictionary[key].remove(value)
            except(ValueError):
                raise ValueError("Value doesn't exist")
        else:
            raise KeyError("Key doesn't exist")

    # function to check if a key exist in the dictionary
    def keyexist(self,key):
        if (key in self.dictionary):
            return True
        else:
            return False

    # function to return list of keys
    def keys(self):
        return list(self.dictionary.keys())

    # function to return the set of values associated with the key
    def members(self,key):
        return self.dictionary[key]

    # function to return all the member values in the the dictionary
    def allmembers(self):
        return list(self.dictionary.values())

    # function to return all the key value pairs
    # Output: list containing key-value pairs in "key: value" format
    def allitems(self):
        items = []
        for key in self.dictionary.keys():
            for member in self.dictionary[key]:
                items.append("{key}: {value}".format(key=key,value=member))
        return items

    # function to remove a key and all of it's members 
    def removeall(self,key):
        if(key in self.dictionary):
            self.dictionary.pop(key)
        else:
            raise KeyError("key doesn't exist")

    # function to clear the dictionary
    def clear(self):
        self.dictionary = {}