# text1~9 중 가장 어휘가 풍부한 코퍼스는?

# import nltk
# nltk.download('book',quiet=True)
# from nltk.book import *


max_text_lexical = len(set(text1))/len(text1)
max_text = text1
texts = [text1,text2,text3,text4,text5,text6,text7,text8,text9]

for text in texts:
    text_lexical = len(set(text))/len(text)
    if max_text_lexical < text_lexical:
        max_text_lexical = text_lexical
        max_text = text
print(text)
#>>> text9