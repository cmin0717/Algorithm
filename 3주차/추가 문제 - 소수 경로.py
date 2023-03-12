from collections import deque
import sys
sys.stdin.readline

n = int(input())

def sosu(x): # 소수를 만드는 함수
    if x == 1:
        return
    else:
        for i in range(2,int(x**0.5)+1):
            if x % i == 0:
                return False
        else: 
            return True

nums = set([i for i in range(1000,10000) if sosu(i)]) # 미리 1000 ~ 10000까지의 소수를 담는다. 
                                                      # 이따 in연산자를 사용하기위해 set자료형으로 저장
for _ in range(n):
    start,end = map(int,input().split())
    check = [0] * 10000 # 방문 체크

    dq = deque()
    dq.append([start,0])
    check[start] = 1

    while dq:
        x,cnt = dq.popleft()

        if x == end:
            print(cnt)
            break

        x = str(x)
        for i in range(4):
            for j in range(10):
                new_num = int(x[:i] + str(j) + x[i+1:]) # 각 자리에 0 ~9 까지 넣어서 아래 조건에 넣어본다.
                if check[new_num] == 0 and new_num in nums: # 방문 한적 없고 소수일경우 진행
                    check[new_num] = 1
                    dq.append([new_num,cnt+1])
    else:
        print("impossible") # break문 안만나고 끝났다면 만족하는 소수가 없다는 뜻
    
