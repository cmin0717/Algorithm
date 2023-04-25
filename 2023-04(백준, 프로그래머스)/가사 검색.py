def solution(words, queries):
    dic1 = {} # ?가 뒤에 있을 경우
    dic2 = {} # ?가 앞에 있을 경우
    
    # 각 word를 단어별로 연관되게 dic에 담는다. dic[0]에는 남은 글자수에따라 나누고 [1]에는 다음 글자에 따라 나눈다.
    for word in set(words): # 중복을 제외하고 돌린다.
        dt1,dt2 = dic1,dic2
        word2 = word[::-1]
        w_l = len(word)
        for i in range(w_l):
            dt1.setdefault(word[i],[{},{}])
            dt1[word[i]][0].setdefault(w_l-i-1,0)
            dt1[word[i]][0][w_l-i-1] += 1
            dt1 = dt1[word[i]][1]
            
            dt2.setdefault(word2[i],[{},{}])
            dt2[word2[i]][0].setdefault(w_l-i-1,0)
            dt2[word2[i]][0][w_l-i-1] += 1
            dt2 = dt2[word2[i]][1]
    
    # 해당 조건에 만족하는 word가 몇개가 있는지 파악하는 함수
    def check(dic, query):
        dt = dic
        for q in range(1,len(query)):
            if query[q] == '?':  # ?가 시작한다면 ?개수만큼 남은 글자가 있는 글자의 개수를 리턴 [0]에 담아두었으니 꺼내 쓴다.
                if dt[0].get(len(query)-q) != None:
                    return dt[0][len(query)-q]
                else:
                    return 0
            if query[q] in dt[1]:
                dt = dt[1][query[q]]
            else:
                return 0
    
    result = {}
    for query in queries:
        # ?로만 이루어진 문자를 따로 처리
        if query[0] == '?' and query[-1] == '?':
            q_len = len(query)
            result[query] = 0
            for k in dic1.keys():
                if q_len-1 in dic1[k][0]:
                    result[query] += dic1[k][0][q_len-1]
        # ?로 시작하는 문자 처리
        elif query[0] == '?':
            q = query[::-1]
            if dic2.get(q[0]) != None:
                result[query] = check(dic2[q[0]], q)
            else:
                result[query] = 0
        # ?로 끝나는 문자 처리
        else:
            if dic1.get(query[0]) != None:
                result[query] = check(dic1[query[0]], query)
            else:
                result[query] = 0
    
    # 담아놓은 결과를 리스트 형태로 리턴한다.
    return [result[q] for q in queries]
        
solution(	["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])