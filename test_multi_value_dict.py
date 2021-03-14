import unittest
from multi_value_dict import MultiValueDictionary

class TestMultiValueDictionary(unittest.TestCase):
    def test_add(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        self.assertEqual(mvd.allitems(), ["foo: bar"])

    def test_add_existing_key(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("foo","baz")
        self.assertEqual(mvd.allitems(), ["foo: bar","foo: baz"])

    def test_add_existing_value(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        with self.assertRaises(ValueError): 
            mvd.add("foo","bar")
       
    def test_remove(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.remove("foo","bar")
        self.assertEqual(mvd.allitems(), [])

    def test_remove_nonexistant_value(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        with self.assertRaises(ValueError):        
            mvd.remove("foo","baz")

    def test_remove_nonexistant_key(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        with self.assertRaises(KeyError):
            mvd.remove("bar","foo")

    def test_keyexist_exists(self):
        mvd = MultiValueDictionary()
        mvd.add("foo", "bar")
        self.assertEqual(mvd.keyexist("foo"), True)
    
    def test_keyexist_nonexistant(self):
        mvd = MultiValueDictionary()
        self.assertEqual(mvd.keyexist("foo"),False)
    
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

    def test_allmembers(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("fizz","buzz")
        mvd.add("fizz","bar")
        mvd.add("boo","mar")
        mvd.add("bar","bar")        
        self.assertEqual(mvd.allmembers(), ["bar","buzz","bar","mar","bar"])

    def test_allmembers_empty(self):
        mvd = MultiValueDictionary()
        self.assertEqual(mvd.allmembers(), [])

    def test_allmembers(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("fizz","buzz")
        mvd.add("fizz","bar")
        mvd.add("boo","mar")
        mvd.add("bar","bar")        
        self.assertEqual(mvd.allitems(), ["foo: bar","fizz: buzz","fizz: bar","boo: mar","bar: bar"])

    def test_allmembers_empty(self):
        mvd = MultiValueDictionary()
        self.assertEqual(mvd.allitems(), [])
    
    def test_removeall_exist(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("fizz","buzz")
        mvd.add("fizz","bar")
        mvd.add("boo","mar")
        mvd.add("bar","bar")
        mvd.removeall("fizz")
        self.assertFalse(mvd.keyexist("fizz"))        
        self.assertEqual(mvd.allitems(), ["foo: bar","boo: mar","bar: bar"])
    
    def test_removeall_nonexistant(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("fizz","buzz")
        mvd.add("fizz","bar")
        mvd.add("boo","mar")
        mvd.add("bar","bar")
        with self.assertRaises(KeyError):
            mvd.removeall("bizz")
        self.assertEqual(mvd.allitems(), ["foo: bar","fizz: buzz","fizz: bar","boo: mar","bar: bar"])
        
    def test_clear(self):
        mvd = MultiValueDictionary()
        mvd.add("foo","bar")
        mvd.add("fizz","buzz")
        mvd.add("fizz","bar")
        mvd.add("boo","mar")
        mvd.add("bar","bar")
        mvd.clear()
        self.assertEqual(mvd.allitems(), [])   

    def test_clear_empty(self):
        mvd = MultiValueDictionary()
        mvd.clear()
        self.assertEqual(mvd.allitems(), [])   