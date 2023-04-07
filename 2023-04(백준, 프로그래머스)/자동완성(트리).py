def solution(words):
    dic = {}
    
    for word in words:
        dt = dic # 하위 트리를 만들기 위해 새로운 변수에 딕셔너리를 담는다.
        for i in word:
            dt.setdefault(i,[0,{}]) # 디폴트값으로 넣어준다. 이미 값이 있다면 적용X
            dt[i][0] += 1
            dt = dt[i][1] # 하위 딕셔너리로 바꾸어준다.
            
    result = 0
    
    for word in words:
        dt = dic
        for i in range(len(word)): # 하나씩 확인하면서 개수가 1이 나올때까지 반복
            if dt[word[i]][0] == 1:
                break
            dt = dt[word[i]][1]
        result += i+1 # 마지막 i값이 그 단어의 입력해야할 총 글자수이다.
        
    return result

# 전형적인 트리 문제이다. 트리를 많이 안풀어봐서 그런가 어렵다...
# 클래스를 구현해서 해결하는 방법도 있다.
# 검색엔진 등에 사용할수 있다. 전화번호 찾기 등등