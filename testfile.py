from core.subeer import call
import unittest



class TestSadiq(unittest.TestCase):

    def test_call(self):
        self.assertRaises(Exception,call,200)


