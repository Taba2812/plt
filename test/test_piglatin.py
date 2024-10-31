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

    def test_plt_word_starting_with_single_consonant(self):
        translator = PigLatin("hello")
        translator.get_phrase()
        self.assertEqual(translator.translate(), "ellohay")

    def test_plt_word_starting_with_more_consonants(self):
        translator = PigLatin("known")
        translator.get_phrase()
        self.assertEqual(translator.translate(), "ownknay")

# ### User Story #5 -- Translating a Word Starting with More Consonants
# The input phrase can be a single word starting with more consonants. In that case, the translator applies the following translation rule:
# * Remove the consonants from the beginning of the word and add them to the end of the word. Finally, append “ay” to the end of the resulting word.
#
# **Requirement:**
# * Implement `PigLatinTranslator.translate(self) -> str` to let the translator translate a word starting with more consonants.
#
# **Example:**
# * The translation of “known” is “ownknay”.