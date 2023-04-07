# 전위/중위/후위 표기법(prefix/infix/postfix)

# 수식 표기법의 종류
# -------------------------------------------------------------------------------------------------
# 1. 전위 표기법 (ex. +AB)

# 연산자를 먼저 표시하고 연산에 필요한 피연산자를 나중에 표기하는 방법.
# -------------------------------------------------------------------------------------------------
# 2. 중위 표기법 (ex. A+B) -사람이 이해하기 쉽게, 사용하기 쉽게 식을 표현하는 방법-

# 연산자를 두 피연산자 사이에 표기하는 방법으로 가장 일반적으로 사용되는 표현 방법.
# 이항 연산자 표현이 적합하다.
# -------------------------------------------------------------------------------------------------
# 3. 후위 표기법 (ex. AB+) -컴퓨터가 연산을 하기 쉽게 표현하는 방법-

# 피연산자를 먼저 표시하고 연산자를 나중에 표시하는 방법.
# 컴파일러가 사용하는 것으로 스택을 사용하는 예들 중 가장 빈번하게 등장.

# -------------------------------------------------------------------------------------------------
# 중위 표기법을 후위 표기법으로 변경시 규칙

# * 괄호가 없는 경우 *
# 1. 숫자는 그대로 출력한다.
# 2. 만약 스택이 비어있다면 연산자를 그냥 스택에 넣는다.
# 3. (스택의 top에 있는 연산자의 우선순위 < 현재 연산자의 우선순위) 이면 현재 연산자를 그냥 스택에 넣는다.
# 4. (스택의 top에 있는 연산자의 우선순위 >= 현재 연산자의 우선순위) 이면 2번 혹은 3번 상황이 될 때까지 pop 하여 출력하고 연산자를 스택에 넣는다.
# 5. 모든 수식을 다 사용했다면 스택이 빌 때까지 pop하여 출력한다.
# 6. 우선순위는 (더하기=빼기) < (곱하기=나누기)이다.

# * 괄호가 있는 경우 *  - 이전 규칙에 아래 규칙을 추가하면 된다.
# 7. 여는 괄호는 스택에 그냥 추가한다.
# 8. 여는 괄호 다음에 오는 연산자는 그냥 스택에 추가한다.
# 9. 닫는 괄호는 여는 괄호가 나올 때까지 스택을 pop 하여 출력한다. 다 출력하고 난 뒤 괄호들은 버린다.
# -------------------------------------------------------------------------------------------------
# 예)
# 1 + (1 + 7)/(2 * 2) 라는 중위 표기법을 후위 표기법으로 바꾸면
# answer: 1, opStack: 
# answer: 1, opStack: +
# answer: 1, opStack: +(
# answer: 11, opStack: +(
# answer: 11, opStack: +(+
# answer: 117, opStack: +(+
# answer: 117+, opStack: +
# answer: 117+, opStack: +/
# answer: 117+, opStack: +/(
# answer: 117+2, opStack: +/(
# answer: 117+2, opStack: +/(*
# answer: 117+22, opStack: +/(*
# answer: 117+22*, opStack: +/
# postfix 최종: 117+22*/+
# 이런식으로 표현 된다.
# -------------------------------------------------------------------------------------------------

import sys
# 연산자의 우선 순위 결정
prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

def convert_to_postfix(S):
    opStack = ArrayStack()
    answer = ''
    
    for w in S :
        if w in prec :
            if opStack.isEmpty() :
                opStack.push(w)
            else :
                if w == '(' :
                    opStack.push(w)
                else :
                    while prec.get(w) <= prec.get(opStack.peek()) :
                        answer += opStack.pop()
                        if opStack.isEmpty() : break
                    opStack.push(w)
        elif w == ')' :
            while opStack.peek() != '(' :
                answer += opStack.pop()
            opStack.pop()
        else :
            answer += w
    
    while not opStack.isEmpty() :
        answer += opStack.pop()
    
    return answer

def calculate(tokens):
    stack = ArrayStack()
    for token in tokens:
        if token == '+':
            stack.push(stack.pop()+stack.pop())
        elif token == '-':
            stack.push(-(stack.pop()-stack.pop()))
        elif token == '*':
            stack.push(stack.pop()*stack.pop())
        elif token == '/':
            rv = stack.pop()
            stack.push(stack.pop()/rv)
        else:
            stack.push(int(token))
    return stack.pop()

infix = sys.stdin.readline().replace("\n", "").replace(" ","")

postfix = convert_to_postfix(infix)

print(f"postfix : {postfix}")

result = calculate(postfix)

print(f"result : {result}")

