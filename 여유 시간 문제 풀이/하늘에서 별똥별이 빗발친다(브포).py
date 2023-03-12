import sys
input = sys.stdin.readline

n,m,l,k = map(int,input().split())
shooting_star = [list(map(int,input().split())) for _ in range(k)]
result = 0

for i in range(k):
    x = shooting_star[i][0]
    for j in range(k):
        y = shooting_star[j][1]
        cnt = 0
        for a,b in shooting_star:
            if x <= a <= x+l and y <= b <= y+l:
                cnt += 1
        result = max(result, cnt)
print(k-result)

# 답을 봤는데 이해가 안간다....이게 왜 답인지....