from heapq import *
import sys
input = sys.stdin.readline

info = list(map(int,input().split()))
cnt = info[2] # 뿅망치 횟수
hp = []

for _ in range(info[0]):
    huge_height = int(input())
    if huge_height >= info[1]: # 센티보다 같거나 큰 거인만 힙에 넣어준다.
        heappush(hp, -huge_height) # 최대값으로 꺼내기위해 -를

while cnt > 0 and hp: # 망치 횟수가 없거나 때릴 거인이 없을때까지

    huge = abs(heappop(hp))
    cnt -= 1

    if huge == 1 and info[1] == 1: # 제일 큰 거인도 1이고 센티도 1이면 더이상 뭘 하는게 의미없기에 break
        heappush(hp, -1)
        break

    if huge//2 >= info[1]:
        heappush(hp, -(huge//2))

if len(hp) == 0:
    print("YES", info[2] - cnt, sep='\n')
else:
    print("NO", abs(heappop(hp)), sep='\n')


