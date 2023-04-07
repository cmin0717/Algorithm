from itertools import *
import sys
input = sys.stdin.readline

# 백트래킹 방법

n = int(input())

city_map = [list(map(int,input().split())) for _ in range(n)]
min_money = 1000000*n + 1

def parade(start,next,cost,visit): # 함수에 시작점, 다음 지점, 누적 비용, 방문한 곳을 넣어준다.
    global min_money
    if len(visit) == n: # 총 방문한 곳이 n개가 될경우
        if city_map[next][start] != 0:
            min_money = min(min_money, cost+city_map[next][start])
        return
    else:
        for i in range(n):
            if i not in visit and city_map[next][i] != 0 and cost < min_money: # 갔다온 곳이라면, 길이 없다면, 현재 비용이 최저보다 높다면
                visit.append(i) # 방문한곳에 넣어주고
                parade(start,i,cost+city_map[next][i],visit) # 다음 지점 방문
                visit.pop() # 다시 목적지를 정하는것니깐 방문한곳 삭제

for i in range(n):
    parade(i,i,0,[i]) # 시작점, 다음목적지, 비용, 갔다온곳을 지정해서 넣어준다.

print(min_money)



# permutations 풀이법 (메모리, 시간 개판남)

# all_map = list(permutations([i for i in range(n)],n))  # 모든 경우의 방문 순서 순열을 뽑아준다.
# for i in all_map:
#     money = 0
#     for j in range(n):
#         if j == n-1:
#             if city_map[i[j]][i[0]] != 0:
#                 money += city_map[i[j]][i[0]]
#                 if min_money > money: min_money = money
#             else: break
#         else:
#             if j != n-1:
#                 if city_map[i[j]][i[j+1]] != 0:
#                     money += city_map[i[j]][i[j+1]]
#                 else: break
# print(min_money)
