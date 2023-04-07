import sys
from heapq import *
input = sys.stdin.readline

for _ in range(int(input())): # 테스트 케이스만큼 진행

    n,d,start = map(int,input().split())
    time = [float('inf')] * (n+1) # 각 지점마다의 최소시간을 저장할 필드
    link = [[] for _ in range(n+1)]

    for _ in range(d):
        a,b,s = map(int,input().split())
        link[b].append([a,s]) # 단반향이므로 한쪽만 저장
    
    h = []
    time[start] = 0
    heappush(h, [0, start]) # 첫감염된 컴퓨터부터 시작

    while h:
        t, idx = heappop(h)

        if time[idx] < t: # 해당 지점을 전에 방문하여 현재 t값보다 작으면 확인할필요가 없다.
            continue
            
        for info in link[idx]:
            new_time = time[idx] + info[1]
            if new_time < time[info[0]]:
                time[info[0]] = new_time
                heappush(h, [new_time, info[0]])

    result = [time[i] for i in range(1,n+1) if time[i] != float('inf')]
    print(len(result), max(result))
