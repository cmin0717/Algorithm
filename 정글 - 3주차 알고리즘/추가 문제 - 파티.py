from heapq import *
import sys
sys.stdin.readline

n,m,party = map(int,input().split())

li = [[] for _ in range(n+1)]

for _ in range(m): # 각 도로의 연결리스트를 저장한다.
    x,y,z = map(int,input().split())
    li[x].append([z,y])

def dis_cost(x): # x출발지에서 각 도시로 가는 최소시간을 구하는 함수
    hq = []
    dis = [float('inf')] * (n+1) # 처음 초기값은 맥스값으로 설정
    dis[x] = 0 # 출발지는 0으로 바꾼다.
    heappush(hq,[0,x])

    while hq:
        cost,idx = heappop(hq)

        if dis[idx] < cost: # pop한 cost보다 원래 값이 더 작다면 전에 더 작은값이 왔다간거니깐 패쓰
            continue

        for i in li[idx]:
            cost = dis[idx] + i[0]
            if cost < dis[i[1]]:
                dis[i[1]] = cost
                heappush(hq,[cost,i[1]])
    return dis

party_dis = dis_cost(party)
result = []

for i in range(1,n+1):
    check = dis_cost(i)
    result.append(check[party] + party_dis[i]) # 집에서 파티장까지 + 파티장에서 집까지 거리를 result리스트에 담는다.

print(max(result))