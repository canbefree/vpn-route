import unittest

from common.apnic import GetApincFileContext,BackupApincFile


class TestApnic(unittest.TestCase):
    def test_sdf(self):
        GetApincFileContext()

    def test_backup_apnic(self):
        BackupApincFile()
