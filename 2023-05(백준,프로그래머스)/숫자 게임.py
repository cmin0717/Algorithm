from collections import deque

def solution(A, B):
    a = deque(sorted(A))
    b = deque(sorted(B))
    
    result = 0
    while b:
        if a[0] < b[0]:
            result += 1
            a.popleft()
            b.popleft()
        else:
            b.popleft()
            
    return result