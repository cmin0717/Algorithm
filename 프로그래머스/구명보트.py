from collections import deque

def solution(people, limit):
    people.sort()
    q = deque(people)
    cnt = 1
    while q:
        total = q.pop()
        for _ in range(len(q)):
            if total + q[0] <= limit:
                total += q.popleft()
            else:
                cnt += 1
                break
    return cnt
