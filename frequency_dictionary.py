import re

class COUNT_FREQ:

    def preprocessing(self, txt):
        self.txt = txt

        self.punct = re.findall('[^\w\s]', self.txt) # 기호 포함
        self.txt = re.sub("[^\w\s]", "", self.txt)
        self.txt = self.txt.split(" ")
        self.word_list = self.txt + self.punct
        return self.word_list # list로 반환

    def counting(self):
        self.freq = {}
        for word in self.word_list:
            if word not in self.freq:
                self.freq[word] = 0
            self.freq[word] += 1

        for self.key, self.value in sorted(self.freq.items(), key = lambda x : -x[1]):
            print(self.value, self.key)


# Driver Code
txt = "그간 코로나19로 인한 장기간 여러 어려움에도 불구하고, 극복의 과정에 최선을 다 해주고 계신 사우님들께 다시 한번 깊은 감사의 인사 드립니다. 사우님들께 최고의 복지로 보답할 수 있도록 노력하겠습니다."
a = COUNT_FREQ()
a.preprocessing(txt)
a.counting()

"""
2 사우님들께
2 .
1 그간
1 코로나19로
1 인한
1 장기간
1 여러
1 어려움에도
1 불구하고
1 극복의
1 과정에
1 최선을
1 다
1 해주고
1 계신
1 다시
1 한번
1 깊은
1 감사의
1 인사
1 드립니다
1 최고의
1 복지로
1 보답할
1 수
1 있도록
1 노력하겠습니다
1 ,
"""