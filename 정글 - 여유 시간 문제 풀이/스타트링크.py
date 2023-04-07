import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

f,s,g,u,d = map(int,input().split())

dp = [float('inf')] * (f+1) # 일단 최대값으로 초기화

def check(idx, cnt):
    if s == g: # 만일 출발점과 도착점이 같다면 도착점에 0값을 넣어주고 바로 종료
        dp[g] = 0
        return
    if idx + u <= f: # 주어진 범위 안에 있다면
        if dp[idx + u] > cnt:
            dp[idx + u] = cnt
            check(idx+u, cnt+1)
    if idx - d >= 1:
        if dp[idx - d] > cnt:
            dp[idx - d] = cnt
            check(idx-d, cnt+1)

if u == 1 and s < g: # U버튼이 1이고 도착점이 출발점보다 높다면 바로구해서 넣어준다
    dp[g] = g-s
elif d == 1 and s > g: # 위와 같음음
    dp[g] = s-g
else:
    check(s,1)

if dp[g] == float('inf'): # 도착지점에 한번도 오지 않았다면 갈수없는곳
    print("use the stairs")
else:
    print(dp[g])
