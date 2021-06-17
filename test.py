import unittest
from modules.decoder import decoder
from modules.encoder import encoder


class TestEncoder(unittest.TestCase):
    def test_encoding(self):
        text = "Test that I know how it sho uld look like!"
        expected_result = "\n—weird—\nTset taht I konw how it sho uld look lkie!\n—weird—\nknow like look Test that"
        self.assertEqual(encoder(text), expected_result)
        
    def test_encoding_len(self):
        text = "I dont know how it will look, but I can check the length of the result!"
        expected_len = 128
        self.assertEqual(len(encoder(text)), expected_len)


class TestDecoder(unittest.TestCase):
    def test_decoding(self):
        text = "\n—weird—\nTset taht I konw how it sho uld look lkie!\n—weird—\nknow like look Test that"
        expected_result = "Test that I know how it sho uld look like!"
        self.assertEqual(decoder(text), expected_result)
        
    def test_wrong_decoding(self):
        text = "\n—weird—\nTset taht I konw how it sho uld look lkie!\n—weird—\nknow like look Test that"
        expected_result = "Wrong test output!"
        self.assertNotEqual(decoder(text), expected_result)


class TestIntegration(unittest.TestCase):
    def test_integration(self):
        text = "Test that I know how it sho uld look like!"
        result = encoder(text)
        self.assertEqual(decoder(result), text)


if __name__ == '__main__':
    unittest.main()