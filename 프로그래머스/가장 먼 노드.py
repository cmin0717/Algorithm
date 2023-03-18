from heapq import *

def solution(n, edge):
    link = [[] for _ in range(n+1)]
    dis = [float('inf')] * (n+1)
    for x,y in edge:
        link[x].append([1,y])
        link[y].append([1,x])
    
    h = []
    heappush(h,[0,1])
    dis[1] = 0
    while h:
        dist, idx = heappop(h)
        
        if dis[idx] < dist: continue
    
        for next in link[idx]:
            new_dist = dis[idx] + next[0]
            if new_dist < dis[next[1]]:
                dis[next[1]] = new_dist
                heappush(h,[new_dist,next[1]])
                
    print(dis.count(max(dis[1:])))

solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])