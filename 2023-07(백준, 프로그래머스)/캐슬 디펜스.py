import sys
from copy import deepcopy
input = sys.stdin.readline

n,m,r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)][::-1]

def find(idx, arr):
    catch = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and (i+1) + abs(j-idx) <= r:
                catch.append([(i+1) + abs(j-idx), i, j])
    if catch:
        catch.sort(key=lambda x: (x[0], x[2]))
        return (catch[0][1], catch[0][2])
    else:
        return False

def move(arr):
    for i in range(n-1):
        arr[i] = arr[i+1]        
    arr[-1] = [0] * m
    return arr

def war(x, y, z, arr):
    turn = 0
    count = 0

    while turn < n:

        die = set()
        for i in [x,y,z]:
            monster = find(i, arr)
            if monster:
                die.add(monster)
        
        for i,j in die:
            arr[i][j] = 0
            count += 1
        
        arr = move(arr)
        turn += 1
    
    return count

result = 0
for i in range(m-2):
    for j in range(i+1,m-1):
        for k in range(j+1,m):
            result = max(result, war(i,j,k,deepcopy(board)))
print(result)