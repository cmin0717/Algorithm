from collections import deque
import sys
input = sys.stdin.readline

n, d, k, c = map(int,input().split())

rail = [int(input()) for _ in range(n)]
rail = rail + rail[:k-1] # 앞과 뒤가 연결된 형태이므로 마지막 인덱스도 확인하기위해

q = deque()
count = 0

for i in rail:
    q.append(i)
    if len(q) == k:
        q.append(c) # 서비스도 같이 넣어준다.
        count = max(len(set(q)), count) # set과 len함수를 통해 몇종류가 있는지 확인
        q.pop() # 아까 넣어준 서비스를 뺀다.
        q.popleft() # 새로운 초밥을 넣기위해 맨앞쪽초밥을 뺀다.
print(count)
