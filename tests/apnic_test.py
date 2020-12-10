'''
    test
'''
import unittest

from common.apnic import genarate_ipinfo_from_file, get_apnic_ipinfo


class TestApnic(unittest.TestCase):
    '''
        class
    '''
    def test_get_ip_data_row(self):
        '''
            test
        '''
        line = r"apnic|CN|ipv4|103.99.56.0|1024|20170821|allocated"
        res = get_apnic_ipinfo(line)
        self.assertEqual(res,("103.99.56.0","255.255.252.0"))

    def test_generate_ip_data_from_file(self):
        file = "./data/apnic_ip/20201210.log"
        genarate_ipinfo_from_file(file)