import sys
input = sys.stdin.readline

n = int(input())
modifys = list(input().rstrip())

maxdp = [[-float('inf')]* n for _ in range(n)] # 최대값 dp
mindp = [[float('inf')]* n for _ in range(n)] # 최소값 dp

# 계산 함수
def calculation(a,b,c):
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    else:
        return a*b

for i in range(0,n,2):
    maxdp[i][i] = int(modifys[i])
    mindp[i][i] = int(modifys[i])

for j in range(2,n,2): # 계산할 수식의 길이
    for i in range(0,n-j,2): # 왼쪽 수식
        for k in range(1, j+1, 2): # 중앙 연산자
            arr = [0,0,0,0]
            # 중앙연산자을 기준으로 왼쪽 오른쪽의 수식을 계산하여 나올 값을 모두 배열에 담는다.
            arr[0] = calculation(maxdp[i][i+k-1], maxdp[i+k+1][i+j], modifys[i+k])
            arr[1] = calculation(maxdp[i][i+k-1], mindp[i+k+1][i+j], modifys[i+k])
            arr[2] = calculation(mindp[i][i+k-1], maxdp[i+k+1][i+j], modifys[i+k])
            arr[3] = calculation(mindp[i][i+k-1], mindp[i+k+1][i+j], modifys[i+k])

            # 왼쪽 수식과 오른쪽 수식에 해당하는 최대값 최소값을 저장
            maxdp[i][i+j] = max(max(arr), maxdp[i][i+j])
            mindp[i][i+j] = min(min(arr), mindp[i][i+j])

# 최대값 출력
print(maxdp[0][n-1])


# 바텀업 방식으로 차근차근 최대값과 최소값을 구해가며 최종적으로 최대값을 구해간다.


    