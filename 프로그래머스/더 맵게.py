from heapq import *

def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while len(scoville) != 1:
        a = heappop(scoville)
        if a >= K : return cnt
        b = heappop(scoville)
        
        cnt += 1
        heappush(scoville, b*2 + a)
    else:
        return cnt if heappop(scoville) >= K else -1