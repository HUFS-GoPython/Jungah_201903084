# NLTK를 임포트하고, text4에서 4자리만 출력하세요
# import nltk
# nltk.download('book',quiet=True)
# from nltk.book import *

print([word for word in text4 if len(word)==4][:4])
#>>> ['life', 'have', 'with', 'than'] 
# 너무 많아서 4개만 출력