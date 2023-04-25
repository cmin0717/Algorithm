def solution(p):
    
    p = list(p) # 문자열을 리스트로 변환
    
    # 해당 p를 u,v로 나누는 함수
    def split(p):
        left,right = 0,0
        for i in range(len(p)):
            if p[i] == '(':
                left += 1
            else:
                right += 1
            # 처음으로 두개의 값이 같아질때가 더이상 분리할수없는 균형잡힌 괄호 문자열이다.
            if left == right:
                return p[:i+1], p[i+1:]
    
    # 해당 괄호 문자열이 올바른 문자열인지 체크
    def check(u):
        temp = 0
        for i in u:
            temp += 1 if i == '(' else -1
            # 음수가 나온다면 올바른 문자열이 될수없다.
            if temp < 0:
                return False
        return True
    
    # 변환 함수
    def convert(u):
        new_u = u[1:-1]
        for i in range(len(new_u)):
            new_u[i] = '(' if new_u[i] == ')' else ')'
        return new_u
    
    # 전체적인 알고리즘 함수
    def result(p):
        if p:
            u,v = split(p)
        else:
            return p
        
        if check(u):
            return u+result(v)
        else:
            new_u = convert(u)
            return ['('] + result(v) + [')'] + new_u
    
    return ''.join(result(p))

solution("()))((()")