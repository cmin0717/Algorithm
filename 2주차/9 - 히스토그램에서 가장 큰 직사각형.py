import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    n = nums[0]
    if n == 0:
        break
    arr = nums[1:]

    stack = []
    max_area = 0

    for i in range(len(arr)):
        if not stack: # 아무것도 없으면 stack에 바로 넣어준다.
            stack.append(i)
            continue
        if arr[stack[-1]] <= arr[i]: # 스택에 있는 사각형보다 큰 사각형이라면 그냥 바로 넣어준다.
            stack.append(i)
        elif arr[stack[-1]] > arr[i]:
            while arr[stack[-1]] > arr[i]: # arr[i]가 보다 큰건 다 pop시켜주는데 pop시킬때 계산을 하고 pop한다.
                m = stack.pop()
                if not stack:
                    max_area = max(max_area, arr[m] * i) # 스택에 아무것도 없다면 pop한 arr[m]보다 작은건 없으니깐
                    break                                # arr[m] * 현재 인덱스(i)를 곱한 직사각형을 만든다.
                else:
                     # 예) 2 3 2 1같은 경우 인덱스 0 2가 같은수지만 else와 같이 처리 되므로 인덱스가 0인데 arr[m]과 값이 같다면 스택이 비어있는거처럼 처리
                    if stack[-1] == 0 and arr[0] == arr[m]:
                        max_area = max(max_area, arr[m] * (i))
                    else:
                        # arr[m]보다 작은 사각형 부터 arr[m]까지의 사각형을 구하고 *arr[m]해준 값을 저장
                        max_area = max(max_area, arr[m] * (i-stack[-1]-1)) 
            stack.append(i)

    while stack: # for문이 끝나고 남아 있는 stack처리
        m = stack.pop()
        if not stack:
            max_area = max(max_area, arr[m] * n)
        else:
            max_area = max(max_area, arr[m] * (n-stack[-1]-1))

    print(max_area)

# 스택과 인덱스를 이용하여 풀어보았다.
# 스택에 사각형을 하나씩 넣다가 stack[-1]보다 작은 값이 들어와야한다면 stack[-1] * (stack[-2]~stack[-1]까지의 인덱스를 구해)값을 저장
# 이런식으로 계속 최대값을 수정해가며 구현
# 어렵....
