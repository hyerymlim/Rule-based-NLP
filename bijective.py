"""
Q. Extract bijective phrases 


1. Statistics 

NUM_LINES 
NUM_SRC_TOKENS
NUM_TGT_TOKENS
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC
NUM_TOKENS_EQUAL_IN_LINE
NUM_TOKENS_INEQUAL_IN_LINE

2. Details

MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT Valentine
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('밸런타인', 3, 확률, (4797, 'Bobby Valentine', '바비 밸런타인'))
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('발렌타인', 1, 확률, (9662, 'Dori Valentine', '도리 발렌타인'))
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('발렌틴', 1, 확률, (22104, 'Karen Valentine', '카렌 발렌틴'))


MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC 솔
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ('Soul', 1, 확률, (8810, 'David Soul', '데이비드 솔'))
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ('Sol', 2, 확률, (40956, 'Sol Bamba', '솔 밤바'))
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ('Saul', 2, 확률 (39096, 'Saul Perlmutter', '솔 펄머터'))
"""

def statistics(fname):
    fout = open(f"{fname}.bijective", "w")
    with open(fname) as fo:
        
        cnt = 0
        cnt_equal = 0 # 토큰수가 같은 라인 수
        cnt_unequal = 0 # 토큰수가 다른 라인 수
        multi_dic_src = 0 
        multi_dic_tgt = 0
       
        # 리스트
        src_tokens = []; tgt_tokens = []; equal_ln = []; unequal_ln = []; 
        # 딕셔너리 
        dic_src = dict(); dic_tgt = dict(); ln_inform_src = dict(); ln_inform_tgt = dict()
            
        for ln, line in enumerate(fo, 1):
            src, tgt = line[:-1].split("\t")
            cnt += 1
              
            src_tokens.append(src)
            tgt_tokens.append(tgt)
            
            if len(src.split()) == len(tgt.split()):
                cnt_equal += 1
                equal_ln.append(ln)
            else:
                cnt_unequal += 1
                unequal_ln.append(ln)
            
            if ln in equal_ln:

                for pair in zip(src.split(), tgt.split()):
                    src_token, tgt_token  = pair 
                    
                    if src_token not in dic_src:
                        dic_src[src_token] = dict()
                    if tgt_token not in dic_src[src_token]:
                        dic_src[src_token][tgt_token] = 0 
                        ln_inform_src[tgt_token] = (ln, src, tgt)
                    dic_src[src_token][tgt_token] += 1
                    
                    if tgt_token not in dic_tgt:
                        dic_tgt[tgt_token] = dict()
                    if src_token not in dic_tgt[tgt_token]:
                        dic_tgt[tgt_token][src_token] = 0
                        ln_inform_tgt[src_token] = (ln, src, tgt)
                    dic_tgt[tgt_token][src_token] += 1
    
    print("DETAILS: SRC_TO_TGT", file = fout)
    for k_src, v_src in dic_src.items():
        print("MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ", k_src, file = fout)
        sorted_freq_dic_src = sorted(v_src.items(), key = lambda x : -x[1])
        v_src_sum = sum(v_src.values())
#         if len(v_src) != 1:
#             multi_dic_src += len(v_src) # MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT 유형 개수
        for key_tgt, value_tgt in sorted_freq_dic_src:            
            pct_tgt = round(value_tgt/v_src_sum, 3)
            if len(v_src) != 1:
                multi_dic_src += value_tgt
            print(f"MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ({key_tgt}, {value_tgt}, 확률: {pct_tgt}, {ln_inform_src[key_tgt]})", file = fout)
        print("\n", file = fout)

    print("\nDETAILS: TGT_TO_SRC", file = fout)     
    for k_tgt, v_tgt in dic_tgt.items():
        print("MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ", k_tgt, file = fout)
        sorted_freq_dic_tgt = sorted(v_tgt.items(), key = lambda x : -x[1])
        v_tgt_sum = sum(v_tgt.values())

        for key_src, value_src in sorted_freq_dic_tgt:
            pct_src = round(value_src/v_tgt_sum, 3)
            if len(v_tgt) != 1:
                multi_dic_tgt += value_src            
            print(f"MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ({key_src}, {value_src}, 확률: {pct_src}, {ln_inform_tgt[key_src]})", file = fout)
        print("\n", file = fout)

    num_src_tokens = " ".join(src_tokens).split()
    num_tgt_tokens = " ".join(tgt_tokens).split()

    print("\nSTATISTICS", file = fout)
    print("NUM_LINES:", cnt, sep = "\t", file = fout)
    print("NUM_SRC_TOKENS:", len(num_src_tokens), sep = "\t", file = fout)
    print("NUM_TGT_TOKENS:", len(num_tgt_tokens), sep = "\t", file = fout)
    print("MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT:", multi_dic_src, sep = "\t", file = fout)
    print("MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC:", multi_dic_tgt, sep = "\t", file = fout)
    print("NUM_TOKENS_EQUAL_IN_LINE:", cnt_equal, sep = "\t", file = fout)
    print("NUM_TOKENS_INEQUAL_IN_LINE:", cnt_unequal, sep = "\t", file = fout)
    
    fout.close()

# Driver Code
print("1. Statistics")
statistics("06.enko.dict.person")
print("\n")
print("2. Details")
src_to_tgt("06.enko.dict.person", "Valentine")
print("\n")
tgt_to_src("06.enko.dict.person", "존")

"""
1. Statistics
NUM_LINES:	48391
NUM_SRC_TOKENS:	98255	UNIQUE: 42405
NUM_TGT_TOKENS:	91921	UNIQUE: 43658
NUM_TOKENS_EQUAL_IN_LINE:	42058
NUM_TOKENS_INEQUAL_IN_LINE:	6333


2. Details
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT Valentine
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('밸런타인', 3, 확률: 0.6, ('4797', 'Bobby Valentine', '바비 밸런타인'))
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('발렌타인', 1, 확률: 0.2, ('9662', 'Dori Valentine', '도리 발렌타인'))
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('발렌틴', 1, 확률: 0.2, ('22104', 'Karen Valentine', '카렌 발렌틴'))


MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC 존
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ('John', 456, 확률: 0.931, ('76', 'AbdellFattah John Jandali', '압둘파타 존 잔달리'))
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ('Jon', 30, 확률: 0.061, ('14335', 'H. Jon Benjamin', 'H. 존 벤저민'))
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ('Zoon', 1, 확률: 0.002, ('17650', 'Jacques Zoon', '야크 존'))
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ('Joan', 1, 확률: 0.002, ('19501', 'Joan Benoit Samuelson', '존 베노이트 사무엘손'))
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ('Jón', 1, 확률: 0.002, ('21615', 'Jón Atli Jónasson', '존 아틀리 조나손'))
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ('Zun', 1, 확률: 0.002, ('27227', 'Liu Zun', '유 존'))
"""


