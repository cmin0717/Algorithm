from heapq import *
import sys
input = sys.stdin.readline

k,n = map(int,input().split())
sosu = list(map(int,input().split()))
result = []

for i in sosu:
    heappush(result, i) # 입력 받은 소수를 heap에 넣어준다.

for _ in range(n):
    num = heappop(result) # heap에 최소값을 뺴온다.

    for i in range(k):
        new_num = num * sosu[i] # 빼온 num와 처음 주어진 소수들을 곱해서 다시 heap에 넣어준다. 
        heappush(result, new_num)
        if num % sosu[i] == 0: # num를 나눌수 있는 소수가 나오면 이후 소수들은 중복이 되므로 break
            break

print(num)

# result = [0] * 1000000

# for i in sosu:
#     result[i] = 1

# for x in range(2,len(result)):
#     if result[x] == 0:
#         for y in sosu:
#             if x % y == 0 and result[x//y] == 1:
#                 result[x] = 1
#                 break
# cnt = 0
# for z in range(len(result)):
#     if result[z] == 1:
#         cnt += 1
#     if cnt == n:
#         print(z)
#         break

# 예제는 맞는데 제출은 실패