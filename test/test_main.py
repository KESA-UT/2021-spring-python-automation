import unittest
import sys
sys.path.append('../')
from src.main import getAccountInformation
import io

class TestMain(unittest.TestCase):

    def test_getAccountInformation1(self):
        print("-------------------------------------------------------")
        print("Testing Account Information in main.py")
        accountInfo = getAccountInformation() # None
        self.assertIsNotNone(accountInfo)
        self.assertTrue(type(accountInfo) is type({}))
        self.assertEqual(accountInfo["account_number"], "PA36CXRKP79V")
        print("test_ex done")
        print("-------------------------------------------------------", end="\n\n")