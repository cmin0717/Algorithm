n = input()

stack = []
result = 0  # 계산된 값을 저장하는 변수
cnt = 1 # 값을 계산하기 위한 변수

for i in range(len(n)):  # 괄호를 열때 계산을 하고 닫을때 저장 하는 형태로 진행
    if n[i] == '(':        
        stack.append(n[i])
        cnt *= 2  # '(' 니깐 * 2
    elif n[i] == '[':
        stack.append(n[i])
        cnt *= 3 # 위와 같다.
    elif n[i] == ')':                     # 만일 stack[-1] == '(' or not stack 해버리면 index오류가 뜬다. 조심하자
        if not stack or stack[-1] == '[': # ')' 가 나오면 안되는 상황에서 나오면 0 출력
            result = 0
            break
        if n[i-1] == '(': # 바로 전에 '(' 이었다면 여태 계산한 cnt값을 result에 넣어준다.
            result += cnt  # 만일 '(' 이게 바로전에 없었다면 전에 값을 result에 넣어주었기에 아래 절차만 진행
        cnt = cnt // 2 # 닫는 기호가 나오면 pop 진행, cnt는 다시 나누어 준다.
        stack.pop()
    else:
        if not stack or stack[-1] == '(': # 위와 동일하다.
            result = 0
            break
        if n[i-1] == '[':
            result += cnt
        cnt = cnt // 3
        stack.pop()

if stack: # 진행이 끝났는데 stack에 원소가 남아있다면 잘못된 괄호열이므로 result값을 0으로 변경
    result = 0
print(result) 

# 풀이 아이디어를 생각하지 못했다...인터넷 풀이 보고도 한참 걸림