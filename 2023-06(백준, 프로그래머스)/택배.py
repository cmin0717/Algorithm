import sys
input = sys.stdin.readline

n, m = map(int,input().split())
count = int(input())
boxs = [list(map(int, input().split())) for _ in range(count)]
boxs.sort(key=lambda x: x[1])

truck = [m] * (n+1)
total = 0

for s,e,w in boxs:
    check = m+1
    for i in range(s,e):
        num = truck[i] if truck[i]-w < 0 else w
        check = min(check, num)
    for i in range(s,e):
        truck[i] -= check
    total += check
print(total)
