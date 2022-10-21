#Q. 주어진 문자열을 pl사전에 나오는 key의 value로 치환해 주세요. 
import re

def sol1(pl, txt):
    for i in pl:
        for m in re.finditer(i, txt):
            txt = re.sub(i, pl[i], txt)

def sol2(pl, txt):
    maxlen = len(max(pl, key = len)) # key의 길이가 max일 때, max(pl, key = len) 해당 key의 length를 반환
    print(maxlen) 

    i=0

    while i < len(txt): # 시작 문자열이 txt의 길이보다 작을 때
        for j in range(min(len(txt), maxlen + i), i, -1): # -1은 역순을 의미 즉, 작은것부터
            ngram = txt[i:j]
            #print(ngram)
            
            if ngram in pl:
                txt = txt[:i] + pl[ngram] + txt[j:]
                i += len(pl[ngram])
                break
        else:
            i += 1
                
    print(txt)

# Driver Code
pl = {"aaa": "AA", "bbb": "BBBBB"}
txt = "sdskjld aaadskkkk fdfdf qqqbbbwqmf"

print(sol1(pl, txt))
print(sol2(pl, txt))