# 다음은 문자열을 입력받아 역 순서의 문자열을 리턴하는 프로그램이다. 빈칸을 채우시오
# import nltk
# nltk.download('book',quiet=True)
# from nltk.book import *


def reverse(L,a):
    n = len(L)
    if a < n-1 :
        L[a],L[n-a-1] = L[n-a-1],L[a]
        reverse(L,a+1)

L = list(input('문자열을 입력하세요:')) #문자열 입력받기
reverse(L,0)
print("".join(str(x) for x in L)) #역 순서의 문자열 출력

# 다 못풀었음...