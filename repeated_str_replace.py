# Q. 주어진 txt에서 2개 초과로 반복되는 문자들을(예.aaa) 대문자 1개로(예.A) 치환하여 tgt와 같이 출력해 주세요.  
import re

# solution1
def func1(txt):
    k = 0
    for m in re.finditer("(.)\\1{2,}", txt): # 문자열 2개 이상 반복
        i,j = m.start(), m.end()
        a = m.group()
        b = a[0].upper()
        
        txt = txt[:i+k] + b + txt[j+k:]
        
        k += len(b) - len(a)
    print(txt)

def func2(txt):
    a = txt.group()
    b = a[0].upper()
    return b

# Driver Code
# func1
txt = "sdskjld aaadskkkk fdfdmmmmmkkf qqqbbbwqmfff"
out = "sdskjld AdsK fdfdMkkf QBwqmF"

print(func1(txt))

# func2
txt = re.sub("(.)\\1{2,}", func2, txt)
print(txt)