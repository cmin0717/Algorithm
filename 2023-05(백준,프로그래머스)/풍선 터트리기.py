from collections import deque

def solution(a):
    result = 0
    
    # 왼쪽 최소값(처음에는 무한수를 넣어준다.)
    left = float('inf')
    # 오른쪽은 a를 정렬시키고 맨뒤에 무한수를 넣어준다. 맨마지막 수를 비교할때 사용하려고
    right_list = deque(sorted(a) + [float('inf')])
    # 방문했던 애들을 모아둔다.
    visit = set()

    for num in a:
        # 방문 체크
        visit.add(num)

        # 오른쪽 최소값을 설정(이미 지나간 애들은 pop시킨다.)
        right = right_list[0]
        while right in visit:
            right_list.popleft()
            right = right_list[0]
        
        # 현재 숫자가 왼쪽,오른쪽이 둘다 작지만 않다면 +1해준다.
        if not(left < num and num >right):
            result += 1
        
        # 왼쪽 최소값 세팅
        left = min(num, left)
    
    print(result)

solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33])