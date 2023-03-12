from collections import deque

n = int(input())

cards = deque([i for i in range(1,n+1)])

while len(cards) > 1:
    cards.popleft()
    cards.rotate(-1)
    # cards.append(cards.popleft()) 이렇게 한줄로 끝낼수도 있을듯하다.

print(*cards)
