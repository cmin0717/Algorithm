from itertools import permutations

def solution(user_id, banned_id):
    
    check_list = list(permutations(user_id,len(banned_id))) # 순열을 이용하여 모든 조합을 뽑는다
    
    def check(x,y): # x,y가 불량아이디에 매핑이 되는지 확인
        if len(x) != len(y):
            return False
        for k in range(len(x)):
            if y[k] != '*' and x[k] != y[k]:
                return False
        return True
    
    result = set()
    for ids in check_list:
        for b_i in range(len(banned_id)):
            if not check(ids[b_i], banned_id[b_i]): # 하나라도 맞지 않으면 패쓰
                break
        else:
            result.add(''.join(sorted(ids))) # 다 맞는다면 정렬후 하나의 문자열로 변환후 set자료형에 넣는다.

    return len(result) # set자료형에서 중복을 거르고 남은 애들만 출력

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])