import sys
input = sys.stdin.readline

n = int(input())
idx = int(input())

start = 1 # 제일 작은값이 1이니깐 1시작
end = n**2 # 제일 큰값은 n*n이니깐 end는 n*n

def check(num): # 주어진 num보다 작은 수를 찾는 함수
    cnt = 0
    for i in range(1,n+1): # 각 행이 1 ~ n의 곱으로 이루어 졌기에 num // i(행) 의 값이 num보다 작은 각행의 숫자개수이다.
        cnt += min(num // i, n) # min함수를 사용한 이유는 만약 num // i가 n을 넘어갈수도 있기떄문에 
    return cnt                  # 각 행의 숫자의 개수가 n을 넘어갈 수 없기에 min함수 사용

while start <= end:
    mid = (start + end) // 2
    if check(mid) >= idx: # mid보다 작은수가 주어진 idx보다 많다면 범위를 낮추어 다시 확인
        end = mid - 1
    else:
        start = mid + 1

print(start) # 본인 보다 작은값이 idx-1개 있는 수중에서 작은값을 가져와야하기에 start출력

# 문제를 어떻게 접근할지 되게어려웠다.
# 결국 인덱스 x번이라는 말이 x 인덱스에 해당하는 수보다 작은수가 x-1개 있다는 말이다.
# 수를 정해주고 배열에서 그 수보다 작은수가 몇개인지 파악해가며 자신보다 작은수가 x-1개있는 수중에서 최소값을 구하면된다.
# x-1개 있는 수중에 최소값이 실제로 배열에 존재하는 수이기 때문에