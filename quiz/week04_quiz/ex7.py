# text4에서는 한 번 출현하지만 text3에서는 여러번 출현하는 단어는 몇개인지 출력
# import nltk
# nltk.download('book',quiet=True)
# from nltk.book import *

freq4 = FreqDist(text4)
freq3 = FreqDist(text3)
once_text4 = freq4.hapaxes()

arr = [word for word in once_text4 if freq3[word] > 1]
print(len(arr))

#>>> 120