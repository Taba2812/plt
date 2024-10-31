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
        if self.phrase == "": return "nil"
        words = self.phrase.split()
        translations = ""
        for word in words:
            composite = word.split('-')
            print(composite)
            for i, part in enumerate(composite):
                translation = part
                phrase_length = len(self.phrase)

                if translation[0] in self.vowels:
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
                    if len(composite) > 1 and i < len(composite) - 1:
                        translation += "-"
                if len(translations) == 0: translations = translations + translation
                else:
                    if len(composite) > 1: translations = translations + translation
                    else: translations = translations + " " + translation
        return translations

"""
### User Story #6 -- Translating a Phrase Containing More Words
The input phrase can contain more words (separated by white spaces). In that case, the translator applies the translation rules (reported in User Stories 3-5) to the single words. Moreover, for composite words (those separated by a “-”), the translation rules apply to the single words.

**Requirement:** 
* Implement `PigLatinTranslator.translate(self) -> str` to let the translator translate a phrase containing more words, as well as composite words. 

**Examples:** 
* The translation of “hello world” is “ellohay orldway”. 
* The translation of “well-being” is “ellway-eingbay”.

"""