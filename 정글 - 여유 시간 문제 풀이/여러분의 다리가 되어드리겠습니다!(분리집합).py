import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
check = [1] * (n+1) # 방문체크
link = [[] for _ in range(n+1)] # 연결리스트

for _ in range(n-2):
    x,y = map(int,input().split())
    # 양방향 통행이므로 양쪽다 넣어준다.
    link[x].append(y)
    link[y].append(x)
# 1번 부터 출발
q = deque([1]) 
check[1] = 0

while q:
    idx = q.popleft()
    for i in link[idx]: # 해당 연결리스트중 방문하지 않은 지점은 큐에 추가
        if check[i]:
            check[i] = 0
            q.append(i)

for i in range(1,n+1):
    if check[i]:
        # 아무 다리나 출력해도 되기에 무조건 1번이랑만 연결해도 괜찮다.
        # 1번 부터 연결리스트를 타고 방문했는데 방문체크가 안되어 있다면 1번과 연결되지 않은것이다.
        # 그렇기에 1번과 방문하지 않은곳 1곳만 연결하는 다리를 만들어주면 된다.
        print(1,i)
        break

    