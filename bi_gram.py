# Q. 주어진 txt에서 (1)어절단위의 bi-gram과 (2)음절단위의 bi-gram에 대한 빈도수를 추출 후, bi-gram에 대한 빈도수를 역순으로 정렬해 주세요.
import re

# 음절 단위 bi-gram
def bi_gram_syll(txt):
    bigrams = {}

    for i in range(len(txt) - 1):
        syll = txt[i:i+2]
        if not syll in bigrams:
            bigrams[syll] = 0
        bigrams[syll] += 1

    for key, value in sorted(bigrams.items(), key = lambda x : -x[1]):
        print(value, key)

def bi_gram_word(txt):
    bigrams = {}

    txt = txt.split() 
    for i in range(len(txt) - 1):
        word = (txt[i], txt[i+1])
        if not word in bigrams:
            bigrams[word] = 0
            bigrams[word] += 1

    for key, value in sorted(bigrams.items(), key = lambda x : -x[1]):
        print(value, *key, sep = "\t")

# Driver code
txt = "Biden, who met with Andersson and Finnish President Sauli Niinisto in the Oval Office before making public remarks, did not reference any specific security measures the United States would provide the two countries before their membership is finalized. The application period is seen as a particularly vulnerable one, because the two countries are defying years of Russian threats against joining NATO but don’t yet fall under the alliance’s security umbrella."
print(bi_gram_syll(txt))
print(bi_gram_word(txt))
