from heapq import *
import sys

input = sys.stdin.readline

n = int(input())

cards = []
result = 0

for _ in range(n):
    num = int(input())
    heappush(cards, num)

while len(cards) != 1: # 카드가 1개이하로 있다면 다 확인한거다.
    card_1 = heappop(cards) # 결국 가장 적게 비교하려면 계속 최소값끼리 비교해가면 된다.
    card_2 = heappop(cards)

    sum_cards = card_1 + card_2
    result += sum_cards
    
    heappush(cards, sum_cards)

print(result)
