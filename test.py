import unittest

from encryption import encryption


class XorTest(unittest.TestCase):

    def test_xor_1(self):
        input_text = 'hello world'
        key = 'key'
        self.assertNotEqual(input_text, encryption(input_text, key))
