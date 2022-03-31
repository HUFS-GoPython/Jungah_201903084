# text4에서 democracy는 몇 번 나오는 지 출력
# import nltk
# nltk.download('book',quiet=True)
# from nltk.book import *

freq4 = FreqDist(text4)
print(freq4['democracy'])

#>>> 65