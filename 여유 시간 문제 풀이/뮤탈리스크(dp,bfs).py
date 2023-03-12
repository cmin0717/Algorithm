from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())

scv = list(map(int,input().split())) + [0] * (3-n) # dp을 사용하기 위해 scv최대 개수인 3개로 맞추어 준다.

h = max(scv) +1 # 체력이 제일 많은 scv구함 인덱스 때문에 +1 한다.
dp = [[[0] * h for _ in range(h)] for _ in range(h)] # 체력이 제일 큰 scv로 3차 배열 생성
result = [] 

def check(x,y,z,cnt):
    if x+y+z == 0:
        result.append(cnt)
        return
    
    if dp[x][y][z] <= cnt and dp[x][y][z] != 0: # dp값 보다 현재 cnt가 같거나 크고 한번이라도 왔던 곳이면 패쓰
        return
    
    dp[x][y][z] = cnt # dp값에 현재 cnt값 대입

    for i in permutations([9,3,1], 3): # permutation을 활용하여 조합 생성
        a = max(x-i[0], 0)
        b = max(y-i[1], 0)
        c = max(z-i[2], 0)
        check(a,b,c,cnt+1)

check(scv[0], scv[1], scv[2], 0)
print(min(result))



    
