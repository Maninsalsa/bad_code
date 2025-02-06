import unittest

class TestHelloSlice(unittest.TestCase):
    def setUp(self):
        self.test_string = "Hello World!"
        
    def test_get_hello_slice(self):
        """Test that the slice operation returns 'Hello'"""
        self.assertEqual(get_hello_slice(self.test_string), "Hello")
        
    def test_alternate_slice(self):
        """Test the alternate slice operation returns 'Hello'"""
        self.assertEqual(self.test_string[:-7], "Hello")

if __name__ == '__main__':
    unittest.main()