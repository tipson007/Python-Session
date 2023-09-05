#Interactive English Dictionary

import json
import difflib

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word does not exists, Please double check it"
my_word = input("Enter word: ")
print(translate(my_word))