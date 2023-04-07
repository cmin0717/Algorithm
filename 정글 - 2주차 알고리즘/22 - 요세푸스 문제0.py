from collections import deque

n,k = map(int,input().split())

pp = deque([str(i) for i in range(1,n+1)]) # 마지막에 join 함수를 쓰기 위해 숫자를 str형으로 받았다.
result = []

while len(pp) > 1:
    pp.rotate(-k+1)
    result.append(pp.popleft())
result.append(pp.pop())

print("<{}>".format(', '.join(result))) 
