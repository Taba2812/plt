class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        translation = self.phrase
        phrase_length = len(self.phrase)
        if self.phrase == "": return "nil"
        if self.phrase[phrase_length - 1] == 'y':
            translation += "nay"
        elif self.phrase[phrase_length - 1] in ['a', 'e', 'i', 'o', 'u']:
            translation += "yay"
        else:
            translation += "ay"

        return translation
