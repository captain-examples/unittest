import unittest
import xmlrunner
import random

class TestFunctions(unittest.TestCase):
    def test_truth(self):
        self.assertTrue(True)
    def test_the_falsity(self):
        self.assertTrue(False)
    def test_the_falsity_2(self):
        self.assertTrue(False)
    def test_flaky(self):
        if random.randint(0,9) > 4:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='tmp/'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)
