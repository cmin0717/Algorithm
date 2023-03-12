from heapq import heappush, heappop, heapify
# 다른 언어에서는 heapq을 구현하기 위해 클래스?를 통해 객체를 생성하지만
# 파이썬에서는 그냥 []리스트로 생성가능하다 하지만 원소를 넣어줄때와 빼줄때 heapq 메소드를 사용해야한다.
"""
     1 ---> root : 가장 작은 원소
   /   \
  3     5
 / \   /
4   8 7
""" # 힙에서는 부모노드값이 자식의 노드 값보다 항상 작다.

heap = []

# heap 원소 추가

heappush(heap, 4) # heappush(x, y) : x라는 heap에 y라는 원소 추가
heappush(heap, 1)
heappush(heap, 6)
heappush(heap, 3)
heappush(heap, 8)
heappush(heap, 7)
print(heap)

# heap 원소 삭제

heappop(heap) # heappop(x) : x라는 heap에 최솟값(root)을 삭제
print(heap)

# 기존 리스트를 힙으로 변환

li = [1, 5, 2, 10, -99, 7, 5]
heapify(li) # 새로운 힙 리스트를 만드는게 아니라 기존 리스트를 힙으로 변환하는것이다.
print(li)

# 최대 힙

nums = [4, 1, 7, 3, 8, 5]
heap1 = []
for i in nums:
    heappush(heap1, [-i, i]) # 힙에 넣는 값에 -값을 붙여서 최소값을 최대값으로 저장한다.
while heap1:
    print(heappop(heap1)[1]) # 꺼낼경우에는 같이 저장한 원래값을 출력

# n번째 최소값 / 최대값

def min_max(li,n):
    heap = heapify(li)
    min_num = None
    for i in range(n):
        min_num = heappop(heap)
    return min_num

# from heapq import nlargest,nsmallest  - heapq에서 지원하는 함수를 이용하여 구할수도 있다.
# nlargest(3, [4, 1, 7, 3, 8, 5]) nlargest(x,y) - y라는 힙에서 x번째 큰수를 출력
# nsmallest(3, [4, 1, 7, 3, 8, 5]) 


# Priority Queue 와 Heapq 의 차이

# 1. Priorityqueue 는 객체 내부에 리스트를 보관해서 사용
# 2. PriorityQueue 는 Thread-Safe 하고 heapq는 Non-safe 하기 때문
# 3. Thread Safe 하다는 것은 반드시 확인 절차를 걸쳐야 하기 때문에 확인하는 작업떄문에 더 느리다. (heapq보다 느린 이유)
# 4. Thread-Safe를 요구하는 상황에서는 PriorityQueue
# 5. Thread-Non-Safe 해도 된다면 heapq 를 사용하는 것이 옳다.