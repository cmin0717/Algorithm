# 정렬 알고리즘 종류와 설명

array = [3,5,7,4,2,1,9,8,6]

# 버블 정렬(bubble sort)

# 인접한 두 수를 비교하며 정렬해나가는 방법으로 O(n²)의 느린 성능을 가지고 있습니다.
# 앞에서부터 시작하여 큰 수를 뒤로 보내 뒤가 가장 큰 값을 가지도록 완성해나가는 방법 
# 또는 뒤에서부터 반복하여 앞의 작은 값부터 정렬을 완성해나가는 방법이 있습니다.
def bubble(arr):
    n = len(arr)
    for i in range(n-1): # 맨 마지막값은 비교할 대상이 없기에 n-1을 해주었다.
        for j in range(n-1-i): # -i 를 해주는 이유는 i개만큼 뒤에 정렬 되어있기에 i만큼은 정렬하지 않아도 된다.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubble(array))

# 선택 정렬(Select sort)

# 한 바퀴 돌 때 가장 작은 값을 찾아 맨 앞과 교환하는 방식의 정렬.
# 앞에서부터 정렬해나가는 특성을 가지고 있고 버블 정렬과 마찬가지로 최악의 성능을 가진 알고리즘입니다.
def select(arr):
    n = len(arr)
    for i in range(n):
        min_num_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_num_index]:
                min_num_index = i
            arr[i], arr[min_num_index] = arr[min_num_index], arr[i]
    return arr
print(select(array))

# 삽입 정렬(Inesertion sort) - O(n²)

# 주어진 배열이 차지하고 있는 공간 내에서 값들의 위치만 바꾸기 때문에 O(1)의 공간 복잡도를 가집니다.
# 정렬된 데이터 그룹을 늘려가며 추가되는 데이터는 알맞은 자리에 삽입하는 방식
# 버블 정렬과 선택 정렬과 마찬가지로 최악의 성능인 정렬 알고리즘입니다.
def insertions(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
        # while문을 통해 불필요한 연산은 생략 할수 있다.
        # while 0 < i and arr[i] < arr[i-1]:
        #     arr[i], arr[i-1] = arr[i-1], arr[i]
        #     i -= 1
    return arr
print(insertions(array))

# 병합 정렬(Merge sort)

# 분할 정복과 재귀를 이용한 알고리즘으로 O(n log n)의 시간 복잡도를 가지고 있어 괜찮은 성능을 보여 줍니다.
# 반으로 쪼개고 다시 합치는 과정에서 그룹을 만들어 정렬하게 되며 이 과정에서 2n 개의 공간이 필요합니다.
def merge(arr):
    n = len(arr)
    if n < 2:
        return arr
    mid = n // 2
    low_arr = merge(arr[:mid])
    high_arr = merge(arr[mid:])

    merge_arr = []
    l,h = 0,0
    while l < len(low_arr) and 1 < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merge_arr.append(low_arr[l])
            l += 1
        else:
            merge_arr.append(high_arr[h])
            h += 1
    # 위에서 다 더하지 못한 배열을 추가로 더해준다.
    merge_arr += low_arr[l:]
    merge_arr += high_arr[h:]
    return merge_arr
print(merge(array))

# 퀵 정렬(Quick sort) 파이썬 내장함수도 퀵 정렬이다.

# 병합 정렬과 마찬가지로 분할 정복 알고리즘으로 평균적으로 빠른 속도를 수행합니다.
# 추가적인 메모리가 공간이 필요 없다는 장점을 가졌습니다.
# 병합 정렬은 균등하게 분할하였다면 퀵 정렬은 Pivot을 설정하고 그 기준으로 정렬을 합니다.
# 다른 정렬 알고리즘보다 빠르며 많은 언어의 정렬 내장 함수로 퀵 정렬을 수행합니다.
def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = len(arr) // 2
    start_arr, mid_arr, end_arr = [], [], []
    for i in arr:
        if i > arr[pivot]:
            end_arr.append(i)
        elif i < arr[pivot]:
            start_arr.append(i)
        else:
            mid_arr.append(i)
    return quick(start_arr) + mid_arr + quick(end_arr) # quick(mid_arr)을 안하는 이유는 mid_arr에 같은 값이 들어가면 무한 루프에 빠진다.
print(quick(array))

# 힙 정렬(heapq sort)
# 힙이 어떻게 구성되는지는 알고있어야한다. 무슨 원리로 돌아가는지
# 힙은 부모 노드가 항상 자식 보다 큰 힙을 최대힙, 항상 작은 힙을 최소힙
from heapq import *

arr = [4, 3, 5, 1, 2]
def heap_sort(arr):
    heapify(arr) # 입력받은 리스트를 heap으로 변환
    sort_num = []

    while arr:
        sort_num.append(heappop(arr)) # 최소값을 하나씩 sort_num리스트에 넣어준다.

    return sort_num
print(heap_sort(arr))