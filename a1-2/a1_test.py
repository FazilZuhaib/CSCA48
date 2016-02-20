import unittest
import a1
# create a test matrix variable which is empty.
test = Matrix()
class TestGetValue(unittest.TestCase):
    def test_get_value(self):
    	test.set_val(0,0,1)
        self.assertEqual(
        		a1.test.get_val(0,0),
        		1,
        		"test.get_value or test.set_value failed."
        	)


if __name__ == '__main__':
    unittest.main()
