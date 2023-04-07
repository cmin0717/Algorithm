import sys, copy
input = sys.stdin.readline

r,c,n = map(int,input().split())

# 결국 4가지의 종류가 필요하다.
# 1. 처음 주어진 배열, 2. 올 폭탄 배열
# 3. 올 폭탄에서 1번 배열의 폭탄이 터진 배열, 4. 올 폭탄에서 3번 배열에서 폭탄이 터졌을때의 배열

change = {'.':'O', 'O':'.'}

case1 = [list(map(str,input().rstrip())) for _ in range(r)] # 1번 배열
case2 = [['O']*c for _ in range(r)] # 2번 배열(올폭탄)
case3 = copy.deepcopy(case1)

for i in range(r):
    for j in range(c):
        if case1[i][j] == 'O':
            for x,y in [i+1,j],[i-1,j],[i,j+1],[i,j-1]:
                if 0 <= x < r and 0 <= y < c:
                    case3[x][y] ='O'
case4 = [list(map(lambda x: change[x], i)) for i in case3] # 3번 배열
newcase3 = copy.deepcopy(case3) # 4번 배열

for i in range(r):
    for j in range(c):
        if case3[i][j] == '.':
            for x,y in [i+1,j],[i-1,j],[i,j+1],[i,j-1]:
                if 0 <= x < r and 0 <= y < c and case3[x][y] == 'O':   
                    newcase3[x][y] = '.'
def pr(arr):
    for i in arr:
        print(''.join(i))


if n == 1:
    pr(case1)
elif n % 2 == 0:
    pr(case2)
elif n % 4 == 1:
    pr(newcase3)
else:
    pr(case4)
