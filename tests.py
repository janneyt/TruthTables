import unittest
from truthTables import *


class testLogic(unittest.TestCase):

    def testAnd(self):
        self.assertEqual(logicAnd(True, False), ANDTABLE)
