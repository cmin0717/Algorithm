from collections import deque

def solution(p, l):
    new_p = []
    for i in range(len(p)):
        if i == l:
            new_p.append([1,p[i]])
        else:
            new_p.append([0,p[i]])

    q = deque(new_p)
    cnt = 1
    
    while q:
        max_num = max([i[1] for i in q])
        check,n = q.popleft()
        if n < max_num:
            q.append([check,n])
        else:
            if check == 1:
                return cnt
            else:
                cnt += 1
print(solution([1, 1, 9, 1, 1, 1],0))