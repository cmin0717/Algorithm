import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    dic = {}
    
    def check(num):
        next_num = dic.get(num)
        # 해당 위치에 현재 아무도 배정받지 않았다면 바로 배정
        if next_num == None:
            dic[num] = num+1
            return num
        else:
            # 해당위치에 누군가 이미 배정받았다면 재귀를 통해 배정받을수 있는 위치를 찾는다.
            next_num = check(next_num)
            # 찾았다면 다음위치로 저장
            dic[num] = next_num+1
            return next_num
    
    result = []
    for i in room_number:
        result.append(check(i))
    return result