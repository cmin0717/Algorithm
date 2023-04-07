import sys
from heapq import *
input = sys.stdin.readline

n, jack = map(int, input().split())

cards = list(map(int,input().split()))

result = []
heapify(result)

for i in range(n-2): # 3장을 뽑아야하니깐 그냥 3중 for문을 돌려 heapq에 -를 추가하여 저장
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum_card = cards[i] + cards[j] + cards[k]
            if sum_card <= jack:
                heappush(result, -sum_card) # 값에 -부호를 부여하여 최대값을 인덱스 0자리에 오게 한다.

print(abs(result[0]))
