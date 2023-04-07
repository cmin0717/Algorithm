import sys
from heapq import *
input = sys.stdin.readline

n,m = map(int,input().split())
link = [[]*(n+1) for _ in range(m)]

for _ in range(m): # 입력받은 집하장의 정보를 연결리스트에 저장
    x,y,time = map(int,input().split())
    link[x].append([y, time])
    link[y].append([x, time])

def check(idx): # 출발 집하장에서 각각의 집합장의 최단거리 구하는 함수 구현 
    h = []
    heappush(h,[0,idx,[idx]]) # 어디어디 가는지 체크하기위해 배열을 인자로 넣어준다.
    dist[idx] = 0

    while h:
        dis, idx, arr = heappop(h)

        if dist[idx] < dis:
            continue

        for info in link[idx]:
            new_dist =  info[1] + dist[idx]

            if new_dist < dist[info[0]]: # 최단거리를 찾아서 정보를 바꾸어줄때
                dist[info[0]] = new_dist # 최단거리와
                start[info[0]] = arr + [info[0]] # 집하장 순서도 같이 바꾸어준다.
                heappush(h, [new_dist, info[0], arr + [info[0]]])

for idx in range(1,n+1):
    dist = [float('inf')] * (n+1)
    start = [[]]*(n+1)
    check(idx)
    result = ['-' if i == [] else i[1] for i in start[1:]] # 순서 배열을 이용하여 답 추출
    print(*result)



