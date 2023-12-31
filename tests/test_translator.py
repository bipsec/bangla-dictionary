import json
import unittest
from io import StringIO
from unittest.mock import patch
from scripts.translator import translator


class TestTranslator(unittest.TestCase):
    def test_translator(self):
        translation_output = translator()
        expected_output = """{
    "custom_message": "This is a basic translator.",
    "google_translator_message": "Using Google Translator",
    "translation": ["Cultivation",        "Recently"]}
    """
        self.assertEqual(translation_output, expected_output)



if __name__ == '__main__':
    unittest.main()
