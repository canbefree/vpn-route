from common.get_domain_ip import get_domain_apnic_txt
import unittest

class DomainTest(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def test_domain_apinc_txt(self):
        ip = get_domain_apnic_txt("baidu.com")
        self.assertEqual("39.156.69.79",ip,"yesself")