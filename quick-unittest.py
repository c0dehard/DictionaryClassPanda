import unittest

def add(x, y):
    return x+y


class Testing_AddFunction(unittest.TestCase):
    def testAdd1(self):
        # got_value, expect_value
        self.assertEquals(add(4, 6), 10)


if __name__ == "__main__":
    unittest.main()
    
