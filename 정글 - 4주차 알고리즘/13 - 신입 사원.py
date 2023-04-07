import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    applicant = [tuple(map(int,input().split())) for _ in range(n)] # 튜플 자료형을 사용하면 시간이 단축된다.
    applicant.sort() # 정렬할때 조건을 넣으니깐 시간초과나지만 빼니깐 안난다.
    
    standard_x = applicant[0][0] # 기준점
    standard_y = applicant[0][1]
    count = 1

    for x,y in applicant[1:]:
        if x <= standard_x or y <= standard_y: # 둘중 하나가 기준점보다 낮다면
            standard_x, standard_y = x,y # 새로운 기준점으로 갱신
            count += 1

    print(count)

# 튜플이 리스트보다 메모리를 더 작게 사용한다.
# 생성 속도도 튜플이 훨씬빠르다 이런 이유들로 시간 차이가 나는듯하다.
# 인덱스 접근 속도도 튜플이 조금더 빠르다.