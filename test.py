import unittest

from encryption import encryption


class XorTest(unittest.TestCase):

    def test_xor_1(self):
        input_text = 'hello world'
        key = 'key'
        self.assertNotEqual(input_text, encryption(input_text, key))

    def test_xor_2(self):
        input_text = 'hello world'
        key = 'key'
        output_text = encryption(input_text, key)
        output_text = encryption(output_text, key)
        self.assertEqual(input_text, output_text)

    def test_xor_3(self):
        input_text = 'hello world'
        good_key = 'good key'
        bad_key = 'bad key'
        output_text = encryption(input_text, good_key)
        good_output_text = encryption(output_text, good_key)
        bad_output_text = encryption(output_text, bad_key)
        self.assertEqual(input_text, good_output_text)
        self.assertNotEqual(input_text, bad_output_text)
