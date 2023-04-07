import sys
input = sys.stdin.readline

n = int(input())
honeycomb = list(map(int,input().split()))

result = 0
total = sum(honeycomb)

# 양사이드에는 꼭 벌이나 벌통이 있어야 한다. 그럼 3가지 케이스로 진행된다.

# 벌 - 벌 - 통
case1 = total - honeycomb[0]
check1 = total - honeycomb[0]
for i in range(1,n):
    check1 -= honeycomb[i]
    result = max(result, case1 + check1 - honeycomb[i])
# 통 - 벌 - 벌
case2 = total - honeycomb[-1]
check2 = total - honeycomb[-1]
for i in range(n-2,-1,-1):
    check2 -= honeycomb[i]
    result = max(result, case2 + check2 - honeycomb[i])
# 벌 - 통 - 벌
case3 = total - honeycomb[0] - honeycomb[-1]
for i in range(1,n-1):
    result = max(result, case3 + honeycomb[i])

print(result)