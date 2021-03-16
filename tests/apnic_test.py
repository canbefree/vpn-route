'''
    test
'''
import unittest

from command.init_apnic import get_apnic_data


class TestApnic(unittest.TestCase):
    '''
        class
    '''
    def test_get_apnic_data(self):
        with self.assertRaises(Exception,"123"):
            f = get_apnic_data("https://www.runoob.com/python/python-exceptions.html")
            while True:
                line = next(f)
                print(line)
