from collections import deque

def solution(s):
    
    result = len(s) # 문자의 최대길이는 주어진 순수문자의 길이
    
    for i in range(1,(len(s) // 2)+1): # 1자리부터 최대길이//2만큼 짤라서 확인해본다.
        q = deque([])
        word = ''
        for w in s:
            word += w
            if len(word) == i:
                q.append(word)
                word = ''
        if word:
            q.append(word)
        
        check,cnt,count = [],1,0 
        
        # 각 조건에 맞게 자른 문자열을 하나씩 꺼내서 연속으로 나오는 값은 따로 처리
        while q:
            word = q.popleft()
            if not check or check[-1] != word:
                check.append(word)
                count += len(str(cnt)) if cnt != 1 else 0
                cnt = 1
            else:
                cnt += 1
        if cnt != 1:
            count += len(str(cnt))
        # check에 있는 요소들을 합친 문자열과 연속된 문자 앞에 추가되는 숫자의 길이를 합친것이 결과이다. 그중 작은걸 선택
        result = min(result, len(''.join(check))+count)
    
    return result
            
solution("aabbaccc")