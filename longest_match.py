#Q. 주어진 pl과 src를 사용하여 longest matching을 구현해 주세요. 
def longest_match1(pl, src):
    maxlen = len(max(pl, key = len))

    i = 0

    while i <len(src): 
        for j in range(min(len(src), maxlen + i), i, -1): 
            ngram = src[i:j] 
            #print(ngram) 
            
            if ngram in pl :
                src = src[:i] + pl[ngram] + src[j:] 
                if len(pl[ngram]) < len(ngram):
                    i += len(ngram) - len(pl[ngram])
                else:
                    i += len(pl[ngram])
                    break
        else:
            i += 1
    print(src) #qqq xxxyyy QQr xxxzzzX


def longest_match2(dic, string):        
    maxlen = max([len(k) for k in dic.keys()])
    st = "0" * len(string)

    for j in range(maxlen, 0, -1):
        if j > len(string):
            continue
        offset = 0
        for i in range(0, len(string)-j+1):
            start, end = i+offset, i+j+offset
            cand = string[start:end]
            if "1" in st[start:end]:
                continue
            if cand in dic.keys():
                string = string[:start] + dic[cand] + string[end:]
                st = st[:start] + "1" * len(dic[cand]) + st[end:]
                offset += len(dic[cand]) - len(cand)
                
    return string
    

# Driver Code
pl = { "ab": "xxx", "cde": "yyy", "rr": "QQ", "cdefgh": "zzz", "z" : "X"}
src = "qqq abcde rrr abcdefghz"
print(longest_match1(pl, src))
print(longest_match2(pl, src))