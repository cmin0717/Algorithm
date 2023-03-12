from heapq import *
import sys
input = sys.stdin.readline

n = int(input())

h_o = [list(map(int,input().split())) for _ in range(n)]

d = int(input())

homeffice = []

for i in h_o:  # 집과 사무실의 거리가 주어진 d보다 크다면 뭘해도 안되니깐 패쓰 조건에 맞는 애들만 저장
    if abs(i[0] - i[1]) <= d:
        i.sort() # 저장할때 집 과 사무실의 위치를 정렬후 넣어준다. 집,사무실이 의미가 없기에 상관없다.
        homeffice.append(i)

homeffice.sort(key= lambda x:x[1]) # 넣어준 애들을 집,사무실 중에 큰값을 기준으로 정렬

cnt = 0
check = []

for way in homeffice: 
    if not check:
        heappush(check, way)
    else:
        while check[0][0] + d < way[1]: # way[1] 범위에 벗어난 원소가 check에 있다면 way가 들어갈수 있을때까지 check를 뺴준다.
            heappop(check)
            if not check:
                break
        heappush(check, way) # 조건처리 이후에 원소를 넣어준다.
        cnt = max(cnt, len(check)) # 그때 그때 마다 최대값을 저장

print(cnt)