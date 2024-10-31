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

    def test_plt_phrase_containing_more_words(self):
        translators = [PigLatin("hello world"), PigLatin("well-being")]
        for translator in translators:
            translator.get_phrase()

        self.assertEqual(translators[0].translate(), "ellohay orldway")
        self.assertEqual(translators[1].translate(), "ellway-eingbay")

"""
### User Story #6 -- Translating a Phrase Containing More Words
The input phrase can contain more words (separated by white spaces). In that case, the translator applies the translation rules (reported in User Stories 3-5) to the single words. Moreover, for composite words (those separated by a “-”), the translation rules apply to the single words.

**Requirement:** 
* Implement `PigLatinTranslator.translate(self) -> str` to let the translator translate a phrase containing more words, as well as composite words. 

**Examples:** 
* The translation of “hello world” is “ellohay orldway”. 
* The translation of “well-being” is “ellway-eingbay”.

"""