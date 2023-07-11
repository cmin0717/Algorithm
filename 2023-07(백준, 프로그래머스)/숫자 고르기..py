import sys
input = sys.stdin.readline

n = int(input())
link = [0] + [int(input()) for _ in range(n)]

def dfs(start, next, visit):
    global check
    if next == start:
        check = True
        return visit+[next]
    
    if link[next] not in visit:
        return dfs(start, link[next], visit + [next])
    
result = set()
for i in range(1,n+1):
    check = False
    info= dfs(i, link[i], [])
    if not check: continue

    arr = info

    for num in arr:
        result.add(num)

print(len(result))
for i in sorted(list(result)):
    print(i)

