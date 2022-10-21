import re
def example(filename):
    with open(filename) as fo:
        cnt_pattern = 0
        cnt_dictionary = 0
        k = 0
        
        for ln, line in enumerate(fo, 1):
            src, tgt, *_ = line[:-1].split("\t")
            
            if re.search("(.)\\1{2,}", tgt):
                print("before:", ln, tgt)
                
    ### 패턴기반 문자열 치환
                for m in re.finditer("(.)\\1{2,}", tgt):
                    i,j = m.start(), m.end()
                    a = m.group()
                    b = a[0].upper()
                
                    tgt = tgt[:i+k] + b + tgt[j+k:]
                
                    #k += len(b) - len(a)
                print("after :", ln, tgt)
                cnt_pattern += 1

    ### 사전기반 문자열 치환
            pl = {'머':'무엇을', '드셨':'먹'}
            maxlen = len(max(pl, key = len))
            #print(maxlen)
            i = 0
            if re.search("(드셨)", src): # (드셨)이 있는 문자열 안에서만 치환 적용
                print("before:", ln, src)
                
                while i < len(src):
                    for j in range(min(len(src), maxlen + i), i, -1):
                        ngram = src[i:j]
                        
                        if ngram in pl:
                            src = src[:i] + pl[ngram] + src[j:]
                            i += len(pl[ngram])
                            print("after: ", ln, src)
                            cnt_dictionary += 1
                            break
                    else: #여기서 else의 의미는 for문이 다 돌고 끝났을 때 적용되는 것.
                        i += 1
            
    print("\n")
    print("cnt_pattern: ",cnt_pattern)
    print("cnt_dictionary: ", cnt_dictionary)

"""
before: 2860 forget it pfff
after : 2860 forget it pF
before: 6223 맛있게 드셨습니까
after:  6223 맛있게 먹습니까
before: 6500 맛있는 거 드셨네용
after:  6500 맛있는 거 먹네용
before: 6719 it was tasty? awww cute
after : 6719 it was tasty? aW cute
before: 7131 머 드셨나요
after:  7131 무엇을 드셨나요
after:  7131 무엇을 먹나요
before: 7132 머 드셨어?
after:  7132 무엇을 드셨어?
after:  7132 무엇을 먹어?
before: 7133 머 드셨어요?
after:  7133 무엇을 드셨어요?
after:  7133 무엇을 먹어요?


cnt_pattern:  2
cnt_dictionary:  8
"""