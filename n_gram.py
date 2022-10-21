# N-GRAM 음절 단위
def ngram_syll(n, txt):

    ngrams = {}

    for num in range(1, n+1):
        for i in range(len(txt)-(num-1)):
            syll = txt[i:i+num]
            if not syll in ngrams:
                ngrams[syll] = 0
            ngrams[syll] += 1

        for k, v in sorted(ngrams.items(), key = lambda x : -x[1]):
            print(v, k)

# N-GRAM 음절 단위, 어절 단위
def ngram_word(n, txt):
    txt = re.sub("(?=[^\w\s])", " ", txt)
    txt = txt.split(" ")

    wordList = []
    ngrams = {}

    #n = 1 ### uni-gram
    #n = 2 ### bi-gram
    n = 3 ### tri-gram

    for i in range(len(txt) - (n-1)):
        wordList.append(txt[i:i+n])

    for word in wordList:
        word = tuple(word) # list = unhashable type -> tuple
        if not word in ngrams:
            ngrams[word] = 0
        ngrams[word] = ngrams[word]+1

    for k, v in sorted(ngrams.items(), key = lambda x : -x[1]):
        print(v, *k, sep="\t")

# Driver Code
txt = "Biden, who met with Andersson and Finnish President Sauli Niinisto in the Oval Office before making public remarks, did not reference any specific security measures the United States would provide the two countries before their membership is finalized. The application period is seen as a particularly vulnerable one, because the two countries are defying years of Russian threats against joining NATO but don’t yet fall under the alliance’s security umbrella."
print(ngram_syll(txt))
print(ngram_wrod(txt))
