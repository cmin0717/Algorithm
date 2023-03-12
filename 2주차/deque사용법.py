from collections import deque # deque 라이브러리를 가져와야한다.
# ------------------------------------------------------------------------------------------------------
# deque 생성

nums = deque()
print(nums)

li = [1,2,3,4]
li = deque() # 원래 있던 리스트에 deque를 선언하면 초기화된 상태로 deque선언이 된다.
print(li)

b = [1,2,3,4]
a = deque(b) # deque(x) -> x라는 자료를 deque으로 변경후 지정 변수에 저장
print(a,b,sep='\n') 
# ------------------------------------------------------------------------------------------------------
# deque 사용법

test = deque()
print(test)

# append()  - > 리스트 append와 같다
test.append(5)
test.append(6)
print(test)

# appendleft()  -> 그냥 append와 다르게 앞쪽(왼쪽)부터 추가 한다.
test.appendleft(4)
test.appendleft(3)
print(test)

# extend() -> deque 뒤(오른쪽)에 iterable 객체를 순환하며 값들을 차례로 추가  * 리스트 extend와 같다. *
test.extend([7,8,9])
print(test)
test.append([7,8,9]) # extend와 append의 차이는 통쨰로 넣냐 하나하나 순차적으로 넣냐 차이다
print(test)

# extendleft() -> deque 앞(왼쪽)에 iterable 객체를 순환하며 값들을 차례로 추가 * 순차적으로 넣기에 넣을 자료가 순서가 바뀌어 완성된다. *
test.extendleft([2,1,0])
print(test)

# remove() -> deque 안의 특정 값 삭제
test.remove(4)
print(test)
test.remove(3)
print(test)

# pop() -> 리스트와 같다.
pop_test = test.pop()
print(pop_test, test,sep='\n')

# popleft() - > pop은 오른쪽을 뺴지만 popleft는 왼쪽을 뺸다.

popleft_test = test.popleft()
print(popleft_test, test, sep='\n')

# rotate(x) -> deque 안의 x 만큼 회전 x 가 양수면 우측 원소가 좌측원소로 회전, 음수면 좌측 원소가 우측 원소로 회전
test.rotate(1)
print(test) # rotate(1) -> 1회 우측 원소를 좌측으로 회전
test.rotate(3) # 양수 이므로 3회 우측 원소를 좌측으로 회전
print(test)
test.rotate(-4) # 음수 이므로 4회만큼 좌측 원소를 우측으로 회전
print(test)

# ------------------------------------------------------------------------------------------------------
# 그외에도 clear, copy, index, insert, maxlen(len 함수와 같다.), reverse등 많이 있다.
