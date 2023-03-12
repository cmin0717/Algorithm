from heapq import *
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
start = int(input())

dis = [float('inf')] * (v+1) # 최소 거리를 저장하는곳 일단 초기값을 맥스값으로 설정
li = [[] for _ in range(v+1)] # 연결리스트

for _ in range(e):
    x,y,z = map(int,input().split())
    li[x].append([z,y]) # 단방향이니깐 한쪽에만 넣어준다.

hq = []
dis[start] = 0 # 출발점은 미리 0값 저장
heappush(hq,[0,start]) # 현재 코스트와 출발 지점 추기

while hq:
    cost,idx = heappop(hq)

    if dis[idx] < cost: # 만약 pop한 cost보다 이미 들어가있는값이 더 작다면 패쓰
        continue        # 작다는 소리는 이전에 더 작은값으로 먼저 방문했다는 의미랑 같다.

    for i,j in li[idx]:
        cost = dis[idx] + i # 현재까지 온 cost와 다음 길의 cost을 더해 새로운 cost를 만든다.
        if cost < dis[j]: # 새로운 cost가 dis에 있는 값보다 작다면 실행
            dis[j] = cost
            heappush(hq,[cost, j])

for i in dis[1:]:
    if i == float('inf'): # 만약 dis에 맥스값이 존재한다면 출발점에서 i값까지 가는 길이 없는것이다.
        print('INF')
    else:
        print(i)