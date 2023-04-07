import sys
input = sys.stdin.readline

n,b = map(int,input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

def calculate(arr1,arr2): # 행렬 끼리 제곱시켜주는 함수
    new_arr = [[0]*n for _ in range(n)] # 새로운 n * n크기의 빈 리스트 생성 # [[0]*n]*n으로 형성하면 안된다... 이유는 모르겠음
    for i in range(n):
        for j in range(n):
            for x in range(n):
                new_arr[i][j] += arr1[i][x] * arr2[x][j]
            new_arr[i][j] = new_arr[i][j] % 1000 # 각 자리를 % 1000해주고 저장
    return new_arr

def test(arr,b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                arr[i][j] = arr[i][j] % 1000
        return arr
    if b % 2 == 0:
        m = test(arr, b//2) # 변수에 미리 넣어주고 계산함수에 넣어주어야 중복 실행을 방지
        new_arr = calculate(m, m)
        return new_arr
    else:
        return calculate(test(arr, b-1), arr)

for i in test(matrix,b):
        print(*i)
