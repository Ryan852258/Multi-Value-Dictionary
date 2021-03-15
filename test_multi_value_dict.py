import unittest
from multi_value_dict import MultiValueDictionary

# Unit Tests for MultiValueDictionary class
class TestMultiValueDictionary(unittest.TestCase):
    def test_add(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        self.assertEqual(mvd.all_items(), ["foo: bar"])

    def test_add_existing_key(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("foo","baz")
        self.assertEqual(mvd.all_items(), ["foo: bar","foo: baz"])

    def test_add_existing_value(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        with self.assertRaises(ValueError): 
            mvd.add("foo","bar")
        self.assertEqual(mvd.all_items(),["foo: bar"])
       
    def test_remove(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.remove("foo","bar")
        self.assertEqual(mvd.all_items(), [])
        self.assertEqual(mvd.keys(),[])
        self.assertEqual(mvd.all_members(),[])

    def test_remove_nonexistant_value(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        with self.assertRaises(ValueError):        
            mvd.remove("foo","baz")
        self.assertEqual(mvd.all_items(),["foo: bar"])

    def test_remove_nonexistant_key(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        with self.assertRaises(KeyError):
            mvd.remove("bar","foo")
        self.assertEqual(mvd.all_items(),["foo: bar"])

    def test_key_exists_exists(self):
        mvd = MultiValueDictionary()
        mvd.add("foo", "bar")
        self.assertEqual(mvd.key_exists("foo"), True)
    
    def test_key_exists_nonexistant(self):
        mvd = MultiValueDictionary()
        self.assertEqual(mvd.key_exists("foo"),False)

    def test_value_exists_exists(self):
        mvd = MultiValueDictionary()
        mvd.add("foo", "bar")
        self.assertEqual(mvd.value_exists("foo","bar"), True)
    
    def test_value_exists_nonexistant_key(self):
        mvd = MultiValueDictionary()
        mvd.add("boo", "bar")
        self.assertEqual(mvd.value_exists("foo","bar"),False)

    def test_value_exists_nonexistant_value(self):
        mvd = MultiValueDictionary()
        mvd.add("foo", "baz")
        self.assertEqual(mvd.value_exists("foo","bar"),False)
    
    def test_keys(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("fizz","buzz")
        mvd.add("fizz","bar")
        mvd.add("boo","mar")
        mvd.add("bar","bar")        
        self.assertEqual(mvd.keys(), ["foo","fizz","boo","bar"])

    def test_keys_empty(self):
        mvd = MultiValueDictionary()    
        self.assertEqual(mvd.keys(), [])

    def test_members(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("fizz","buzz")
        mvd.add("fizz","bar")
        mvd.add("boo","mar")
        mvd.add("bar","bar")        
        self.assertEqual(mvd.members("fizz"), ["buzz","bar"])
        self.assertEqual(mvd.members("bar"), ["bar"])
        self.assertEqual(mvd.members("foo"), ["bar"])
        self.assertEqual(mvd.members("boo"), ["mar"])

    def test_members_nonexistant(self):
        mvd = MultiValueDictionary()
        with self.assertRaises(KeyError):        
            mvd.members("fizz")

    def test_all_members(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("fizz","buzz")
        mvd.add("fizz","bar")
        mvd.add("boo","mar")
        mvd.add("bar","bar")        
        self.assertEqual(mvd.all_members(), ["bar","buzz","bar","mar","bar"])

    def test_all_members_empty(self):
        mvd = MultiValueDictionary()
        self.assertEqual(mvd.all_members(), [])

    def test_all_items(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("fizz","buzz")
        mvd.add("fizz","bar")
        mvd.add("boo","mar")
        mvd.add("bar","bar")        
        self.assertEqual(mvd.all_items(), ["foo: bar","fizz: buzz","fizz: bar","boo: mar","bar: bar"])

    def test_all_items_empty(self):
        mvd = MultiValueDictionary()
        self.assertEqual(mvd.all_items(), [])
    
    def test_remove_all_exist(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("fizz","buzz")
        mvd.add("fizz","bar")
        mvd.add("boo","mar")
        mvd.add("bar","bar")
        mvd.remove_all("fizz")
        self.assertFalse(mvd.key_exists("fizz"))        
        self.assertEqual(mvd.all_items(), ["foo: bar","boo: mar","bar: bar"])
    
    def test_remove_all_nonexistant(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("fizz","buzz")
        mvd.add("fizz","bar")
        mvd.add("boo","mar")
        mvd.add("bar","bar")
        with self.assertRaises(KeyError):
            mvd.remove_all("bizz")
        self.assertEqual(mvd.all_items(), ["foo: bar","fizz: buzz","fizz: bar","boo: mar","bar: bar"])
        
    def test_clear(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("fizz","buzz")
        mvd.add("fizz","bar")
        mvd.add("boo","mar")
        mvd.add("bar","bar")
        mvd.clear()
        self.assertEqual(mvd.all_items(), [])   

    def test_clear_empty(self):
        mvd = MultiValueDictionary()
        mvd.clear()
        self.assertEqual(mvd.all_items(), [])   

# run tests on script run
if __name__ == '__main__':
    unittest.main()