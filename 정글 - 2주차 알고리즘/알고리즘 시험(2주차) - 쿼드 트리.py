import sys
input = sys.stdin.readline

n = int(input())

trees = [input().rstrip() for _ in range(n)]

result = ''

def check(x,y,n):
    global result
    standard = trees[x][y]

    for i in range(x,x+n):
        for j in range(y, y+n):
            if trees[i][j] != standard:
                result += '('
                n = n//2
                check(x, y, n)
                check(x, y+n, n)
                check(x+n, y, n)
                check(x+n, y+n, n)
                result += ')'
                return
    result += standard
    
check(0,0,n)
print(result)