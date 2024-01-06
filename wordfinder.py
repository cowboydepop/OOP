"""Word Finder: finds random words from a dictionary."""

import random 
class WordFinder:
    def __init__(self,file):
        """reads word list and reports length"""
        self.file= file
        dict = open(file)
        self.words = file.parse(file)
        print(f"{len(self.words)} words read")

    def parse(self, file):
        return [w.strip() for w in file]
    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):


    def parse(self, file):

        return [w.strip() for w in file
                if w.strip() and not w.startswith("#")]
        
        