import sys
input = sys.stdin.readline

n,m = map(int,input().split())

# 집합 자료형 풀이
memo = {input().rstrip() for _ in range(n)}

for _ in range(m):
    keyword = set(input().rstrip().split(","))
    memo.difference_update(keyword) # memo = memo - keyword는 시간초과뜬다?? 와이??
    print(len(memo))

# 딕셔너리 풀이
cnt = n
memo = {}

for _ in range(n):
    keyword = input().rstrip()
    memo[keyword] = 1

for _ in range(m):
    blog = list(input().rstrip().split(','))
    for node in blog:
        if memo.get(node) == None or memo[node] == 0:
            continue
        else:
            memo[node] = 0
            cnt -= 1
    print(cnt)
