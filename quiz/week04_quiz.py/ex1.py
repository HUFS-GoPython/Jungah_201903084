#문제: text7에서 가장 긴 단어는 몇 자인가?
#import nltk 
#nltk.download('book',quiet=True)
#from nltk.book import *

max_word = text7[0]
for word in text7:
    if len(max_word) < len(word):
        max_word = word
print(len(max_word))

#>>> 24