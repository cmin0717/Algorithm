import heapq,sys
input = sys.stdin.readline

n = int(input())

heap_li = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap_li) == 0:
            print(0)
        else:
            print(abs(heapq.heappop(heap_li)))
    else:
        heapq.heappush(heap_li, -num) # heapq은 최소값을 0인덱스에 두기 떄문에 넣을떄 -를 붙여 최대값을 최소값으로 만든다.
