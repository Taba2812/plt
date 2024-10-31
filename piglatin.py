from fnmatch import translate


class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        translation = self.phrase
        phrase_length = len(self.phrase)

        if self.phrase == "": return "nil"
        elif translation[0] in ['a', 'e', 'i', 'o', 'u']:
            if self.phrase[phrase_length - 1] == 'y': translation += "nay"
            elif self.phrase[phrase_length - 1] in ['a', 'e', 'i', 'o', 'u']: translation += "yay"
            else: translation += "ay"
        else:
            new_translation = translation[1:] + translation[0]
            translation = new_translation + "ay"

        return translation

# ### User Story #4 -- Translating a Word Starting with a Single Consonant
# The input phrase can be a single word starting with a single consonant (note that the "y" letter is considered a consonant). In that case, the translator applies the following translation rule:
# * Remove the consonant from the beginning of the word and add it to the end of the word. Finally, append “ay” to the end of the resulting word.
#
# **Requirement:**
# * Implement `PigLatinTranslator.translate(self) -> str` to let the translator translate a word starting with a single consonant.
#
# **Example:**
# * The translation of “hello” is “ellohay”.