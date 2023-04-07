import sys
input = sys.stdin.readline

n,k = map(int,input().split())

num = input().rstrip()

stack = [num[0]] # 시작하기 전에 일단 제일 앞에 값을 넣고 시작
pop_cnt = 0

for i in range(1,n):
    while pop_cnt != k and stack: # pop_cnt가 k가 되거나 스택이 비어있을 경우까지
        if stack[-1] < num[i]:    # 큰값이 있으면 바꾼다.
            stack.pop()
            pop_cnt += 1
        else:
            if len(stack) < n-k: # 값이 작아도 계속 넣을순 없다. 조건에 해당하면 진행
                stack.append(num[i])
            break
    else:
        stack.append(num[i]) # 더이상 뺼수 없거나 stack이 비어있으면 추가

result = ''
for j in stack:
    result += j
print(result)
