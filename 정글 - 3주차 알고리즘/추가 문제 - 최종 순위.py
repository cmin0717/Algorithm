from collections import deque
import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):

    n = int(input())
    rank = list(map(int,input().split()))
    link = [[] for _ in range(n+1)]
    degree = [0] * (n+1)
    m = int(input())
    if m == 0: # 순위 변동이 없다면 그냥 작년꺼 출력력
        print(*rank)
        continue

    for i in range(n):
        for j in rank[i+1:]: # 작년 등수 기준 자신 보다 등수가 낮은 애들을 연결리스트에 담아주고 진입 차수에 + 1해준다.
            link[rank[i]].append(j)
            degree[j] += 1 # rank[i]보다 작은 애들은 진입 차수를 +1씩해준다. 1등부터 출력해야하니깐

    for _ in range(m):
        x,y = map(int,input().split())
        if y in link[x]: # 순위 변동이 있을때
            link[x].remove(y)
            degree[y] -= 1
            link[y].append(x)
            degree[x] += 1
        else:
            link[y].remove(x)
            degree[x] -= 1
            link[x].append(y)
            degree[y] += 1
            
    dq = deque()
    for l in range(1,n+1):
        if degree[l] == 0:
            dq.append(l)

    result = []
    while dq:
        idx = dq.popleft()
        result.append(idx)
        for i in link[idx]:
            degree[i] -= 1
            if degree[i] == 0:
                dq.append(i)
    if len(result) == n:
        print(*result)
    else:
        print('IMPOSSIBLE')
