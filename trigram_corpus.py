# Q. 주어진 '05.corpus.txt' 코퍼스에서 tri-gram 범위에서 '학교에' 다음에 나올 수 있는 어절들을 구하여 확률이 높은 순으로 나열해 주세요.

import re
import math

class N_GRAM_LM:
    
    # Class Variables
    uni_total = 0; bi_total = 0; tri_total = 0
        
    # init method: open file
    def __init__(self):
        
        self.filename = input('enter file name:')
        print("file \"{}\" read (｡･ω･｡)".format(self.filename))

    # ngram method
    def ngraming(self):

        self.word = input('enter word: ')
        self.ngram = int(input('enter N: ')) # ngram:int
        self.ngram_list = []
        
        with open(self.filename) as self.fo:
            for ln, line in enumerate(self.fo, 1):

                self.word_list = line.split() # 어절 토큰 리스트

                # 전체 ngram -> 분모
                self.word_total = len(self.word_list)

                self.uni_total += self.word_total
                self.bi_total += self.word_total - 1
                self.tri_total += self.word_total - 2

                for n in range(self.ngram):
                    for idx in range(len(self.word_list)-n):
                        if self.word_list[idx] == self.word:
                            self.ngram_list.append(tuple(self.word_list[idx:idx+(n+1)]))

            print("\"{}\"의 {}-gram list 생성 완료 (❀╹◡╹)".format(self.word, self.ngram))

    # frequency method
    def counting(self):
        self.freq = {} 
        for w in self.ngram_list:
            if w not in self.freq:
                self.freq[w] = 0
            self.freq[w] += 1
        sorted_freq_list = sorted(self.freq.items(), key = lambda x : -x[1])
        for key, value in sorted_freq_list:
            print(value, key, sep ="\t")
        print("빈도 구하기 완료 ( ღ'ᴗ'ღ )")
            
    # probability method
    def probability(self):
        sorted_word_list = sorted(self.freq.items(), key = lambda x: -x[1])
        for k, v in sorted_word_list:
            if len(k) == 1:    
                prob = math.log(v / self.uni_total)
            elif len(k) == 2:
                prob = math.log(v / self.bi_total)
            else:
                prob = math.log(v / self.tri_total)
            print(prob, k, sep = "\t")
        print("확률 구하기 완료 ٩(๑>∀<๑)۶")

# Driver Code
# 파일별 instantiation
# 1. open file
a = N_GRAM_LM()
b = N_GRAM_LM()
"""
enter file name:05.corpus.txt
file "05.corpus.txt" read (｡･ω･｡)
enter file name:05.corpus.txt
file "05.corpus.txt" read (｡･ω･｡)
"""

# 2. list of n-gram
a.ngraming()
print("\n")
b.ngraming()
"""
enter word: 학교에
enter N: 3
"학교에"의 3-gram list 생성 완료 (❀╹◡╹)


enter word: 집으로
enter N: 2
"집으로"의 2-gram list 생성 완료 (❀╹◡╹)
"""

# 3. n-gram frequency
a.counting()
print("\n")
b.counting()
"""
97	('학교에',)
5	('학교에', '갈')
3	('학교에', '가지')
3	('학교에', '가는')
3	('학교에', '가야')
2	('학교에', '오지')
2	('학교에', '가고')
2	('학교에', '가는', '것을')
2	('학교에', '갔습니다.')
2	('학교에', '대해')
2	('학교에', '갈', '수')
2	('학교에', '못')
1	('학교에', '지각해')
"""

# 4. n-gram probability
a.probability()
print("\n")
b.probability()
"""
-8.881475415148968	('학교에',)
-11.692155581516461	('학교에', '갈')
-12.202981205282452	('학교에', '가지')
-12.202981205282452	('학교에', '가는')
-12.202981205282452	('학교에', '가야')
-12.608446313390616	('학교에', '오지')
-12.608446313390616	('학교에', '가고')
-12.425505320050034	('학교에', '가는', '것을')
-12.608446313390616	('학교에', '갔습니다.')
-12.608446313390616	('학교에', '대해')
-12.425505320050034	('학교에', '갈', '수')
-12.608446313390616	('학교에', '못')
-13.301593493950561	('학교에', '지각해')
"""
