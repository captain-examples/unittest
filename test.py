import unittest
import xmlrunner

class TestFunctions(unittest.TestCase):
    def test_truth(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='tmp/'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)
