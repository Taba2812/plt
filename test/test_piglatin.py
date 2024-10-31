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

    def test_plt_word_starting_with_vowel(self):
        translators = [PigLatin("any"), PigLatin("apple"), PigLatin("ask")]
        for translator in translators:
            translator.get_phrase()

        self.assertEqual(translators[0].translate(), "anynay")
        self.assertEqual(translators[1].translate(), "appleyay")
        self.assertEqual(translators[2].translate(), "askay")