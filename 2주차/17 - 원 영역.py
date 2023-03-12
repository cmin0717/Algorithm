import sys
input = sys.stdin.readline

n = int(input())

circle = []
for _ in range(n):
    x,y = map(int,input().split())
    circle.append([x-y,'(']) 
    circle.append([x+y,')'])
circle.sort(key= lambda x: (x[0],-ord(x[1]))) # 원의 왼쪽,오른쪽을 저장후 작은수 부터 값이 같다면 ')'닫는 부호 부터로 정렬

cnt = 1 # 여백의 공간도 1로 계산하니깐 시작을 1로
stack = []

for x in range(n*2): # 원을 2개로 나누어서 저장했으므로 n*2로 for문을 돌린다.
    i = circle[x]
    if not stack:
        stack.append([i[0], i[1], 0]) # stack에는 [좌표, 괄호 모양, 원이 연속으로 접하고 있는지 없는지]  # 원이 접하고 있으면 1, 없으면 0
        continue
    if i[1] == ')':
        if stack[-1][2] == 0: # 닫는 괄호가 나왔을때 stack[-1][2]을 파악하여 전에 나왔던 원이 접해 있는지 떨어져있는지에 따라 +를 달리한다.
            cnt += 1
        else:
            cnt += 2
        stack.pop() # 더해줫으니 pop!
        if x != n*2-1 and circle[x+1][0] != i[0]: # pop을해서 다음 원과 접하는지를 파악하기 힘드니 미리 다음 값을 봐서 계속 접해있다면 
            stack[-1][2] = 0                      # stack[-1][2]를 1로 변경해준다.
    else:
        if stack[-1][0] == i[0]: # 여는 괄호가 나왔고 저번 원과 접해있다면 저번 원의 [2]를 1로 변경 후 현재 원 저장
            stack[-1][2] = 1
            stack.append([i[0], i[1], 0])
        else:
            stack.append([i[0], i[1], 0]) # 그렇지 않다면 그냥 현재 원 저장

print(cnt)

# 원으로 생각하지말고 원의 왼쪽을 '('으로 원의 오른쪽을 ')'으로 생각
# 괄호가 ')''(' 이렇게 같은 좌표에 붙어 있다면 서로 접하는 원이다.
# 계속 접하다가 ')' 닫힌 원은 +2 아닌 원은 +1로 계산하면 해결가능하다.