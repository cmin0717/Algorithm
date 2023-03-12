import sys
input = sys.stdin.readline

n = int(input())

result = []

for _ in range(n):
    num = int(input())
    if num == 0:
        result.pop()
    else:
        result.append(num)
        
print(sum(result))