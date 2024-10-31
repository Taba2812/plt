import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_plt_get_phrase(self):
        translator = PigLatin("hello world")
        translator.get_phrase()
        self.assertEqual(translator.get_phrase(), "hello world")

    def test_plt_empty_phrase(self):
        translator = PigLatin("")
        translator.get_phrase()
        translation = translator.translate()
        self.assertEqual(translation, "nil")