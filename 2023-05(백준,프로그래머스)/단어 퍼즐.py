# DP 풀이
def solution(strs, t):
    n, strs = len(t), set(strs)
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    
    for i in range(n):
        for j in range(1,6):
            k = i+j
            if k >= n+1:
                break
            
            if t[i:k] in strs:
                dp[k] = min(dp[i]+1, dp[i+j])
    
    return dp[-1] if dp[-1] != float('inf') else -1


# 큐를 이용하여 BFS로 접근했는데 시간 초과 나온다.
# 범위가 넓지 않아서 왜 나오는지 모르겠다....
# 맞는거 같은데

# 방문 체크를 true, false로 바꾸니 통과했다.....
# 그렇게 차이가 큰가? 딕셔너리도 O(1)아닌가??...
# 딕셔너리가 커지면 다시 해쉬화 하는것에 시간을 많이 사용한건가??...
# 모르겠다...홀란스럽다....엘링 홀란...
from collections import deque
def solution(strs, t):

    strs, q, n = set(strs), deque(), len(t)
    
    part = ''
    for i in t:
        part += i
        if part in strs:
            q.append([1, part])
    
    visit = [False] * n
    while q:
        cnt, word = q.popleft()
        
        if word == t:
            return cnt
        
        word_rest = ''
        for i in range(len(word), min(n, len(word)+5)):
            word_rest += t[i]
            if word_rest in strs:
                new_word = word + word_rest
                if not visit[i]:
                    visit[i] = True
                    q.append([cnt+1, new_word])

    return -1
solution(["a"], "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

