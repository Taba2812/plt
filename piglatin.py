from fnmatch import translate


class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    def get_phrase(self) -> str:
        return self.phrase

    def is_consonant(self, letter: str) -> bool:
        if letter in self.consonants:
            return True
        else:
            return False

    def translate(self) -> str:
        translation = self.phrase
        phrase_length = len(self.phrase)

        if self.phrase == "": return "nil"
        elif translation[0] in self.vowels:
            if self.phrase[phrase_length - 1] == 'y': translation += "nay"
            elif self.phrase[phrase_length - 1] in ['a', 'e', 'i', 'o', 'u']: translation += "yay"
            else: translation += "ay"
        elif translation[0] in self.consonants:
            starting_consonants = ""
            for letter in translation:
                if self.is_consonant(letter): starting_consonants += letter
                else: break
            number_of_consonants = len(starting_consonants)
            new_translation = translation[number_of_consonants:] + starting_consonants
            translation = new_translation + "ay"

        return translation

# ### User Story #5 -- Translating a Word Starting with More Consonants
# The input phrase can be a single word starting with more consonants. In that case, the translator applies the following translation rule:
# * Remove the consonants from the beginning of the word and add them to the end of the word. Finally, append “ay” to the end of the resulting word.
#
# **Requirement:**
# * Implement `PigLatinTranslator.translate(self) -> str` to let the translator translate a word starting with more consonants.
#
# **Example:**
# * The translation of “known” is “ownknay”.