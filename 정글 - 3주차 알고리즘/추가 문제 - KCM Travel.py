from heapq import *
import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n, max_cost, k = map(int,input().split())
    li = [[] for _ in range(n+1)]
    dis = [float('inf')] * (n+1)

    for _ in range(k):
        x,y,c,t = map(int,input().split())
        li[x].append([t,c,y])
    
    hq = []
    dis[1] = 0
    heappush(hq,[0,0,1])
    result = []
    while hq:
        time,cost,idx = heappop(hq)

        if idx == n:
            result.append([time,cost])

        if cost > max_cost:
            continue
        
        for a,b,c in li[idx]:
            time = dis[idx] + a
            dis[c] = time
            heappush(hq,[time,cost+b,c])

    result.sort(key=lambda x:(x,x[1]))
    for i,j in result:
        if j <= max_cost:
            print(i)
            break
    else:
        print('Poor KCM')


# 포기 !