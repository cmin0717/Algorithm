from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
li = [list(map(int,input().split())) for _ in range(m)]
start,end = map(int,input().split())

dis = [float('inf')] * (n+1) # 거리값을 일단 맥스값으로 설정
bus = [[] for _ in range(n+1)]

for a,b,c in li:
    bus[a].append([b,c]) 

hq = []
heappush(hq, [0,start]) # [비용, 노드]를 넣어준다.
dis[start] = 0 # 시작값은 0으로 설정

while hq:
    c,x = heappop(hq)
    if dis[x] < c: # 힙으로 가져온 비용보다 작을경우에는 굳이 안해도 되니깐 continue시킨다. (방문했던 셈이다.)
        continue
    for i in bus[x]:
        c = dis[x] + i[1] # i[1]까지 소요된 비용
        if c < dis[i[0]]: # 비용이 원래 비용보다 작다면 진행
            dis[i[0]] = c # 비용을 바꾸어주고
            heappush(hq, [c, i[0]]) # 진행

print(dis[end])
