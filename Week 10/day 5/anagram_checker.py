import json

class AnagramChecker():
    def __init__(self):
        f = open(r"C:/Users/annak/Desktop/DI_Bootcamp/Week 10/day 5/text.txt", "r")
        self.new_text = f.read().split("\n")
        f.close()


    def is_valid_word(self,word):
        if word in self.new_text:
            return word + " Is a valid word"
        else:
            return word + " Is not a valid word"

ana = AnagramChecker()

print(ana.is_valid_word("blabla"))

    def get_anagrams(self, anagram):



    def is_anagram(self, word1, word2):
        if word1 in self.text:



