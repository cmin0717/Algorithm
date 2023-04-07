from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(m)]
city = [[] for _ in range(n+1)]
check = [0] * (n+1)
check[x] = 1 # 시작점을 미리 방문한곳으로 체크!

for a,b in li:
    city[a].append(b) # 단방향 통행이므로 한쪽에만 넣어준다.

result = []
dq = deque([city[x]+[1]]) # city[x]값과 [-1]에 현재 거리를 넣어준다.

while dq:
    element = dq.popleft()
    # if element[-1] > k:continue  있나 없나 속도 차이가 별로 안난다.
    for i in element[:-1]:
        if check[i] == 0: # 일단 방문을 안한곳만 체크가능하니깐 방문했는지 안했는지 체크
            if element[-1] == k: # 현재거리가 문제에서 원하는 거리 k가 된다면 result에 넣어준다.
                result.append(i)
                check[i] = 1 # 방문했으니 체크
            else:
                check[i] = 1 # 중복을 막기 위해 pop되기전에 방문한곳 체크
                dq.append(city[i] + [element[-1] + 1]) # 다음 곳에 갈때는 현재거리에 +1해서 넣어준다.

if len(result) == 0:
    print(-1)
else:
    result.sort()
    print(*result,sep='\n')


# 다익스트라 풀이법
# from heapq import * 
# import sys
# input = sys.stdin.readline

# n,m,k,start = map(int,input().split())

# dis = [float('inf')] * (n+1)
# li = [[] for _ in range(n+1)]

# for _ in range(m):
#     x,y = map(int,input().split())
#     li[x].append([1,y])

# dis[start] = 0
# hq = []
# heappush(hq,[0,start])

# while hq:
#     c,idx = heappop(hq)

#     if dis[idx] < c:
#         continue

#     for cost,i in li[idx]:
#         c = dis[idx] + cost
#         if c < dis[i]:
#             dis[i] = c
#             heappush(hq,[c,i])
            
# for i in range(1,n+1):
#     if dis[i] == k:
#         print(i)
# if k not in set(dis):
#     print(-1)