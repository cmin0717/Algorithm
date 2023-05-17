from collections import deque

def solution(s):
    
    def check(word):
        # 소,중,대 괄호에 관한 배열생성
        s,m,l = [],[],[]

        # 각 문자열을 조건에 맞게 처리해가면 올바른 괄호가 아니라면 즉시 False 리턴
        for idx in range(len(word)):
            i = word[idx]
            if i == '[':
                l.append(False)
            elif i == ']':
                if l and word[idx-1] not in ['{','(']:
                    l.pop()
                else:
                    return False
            elif i == '{':
                m.append(False)
            elif i == '}':
                if m and word[idx-1] not in ['[','(']:
                    m.pop()
                else:
                    return False
            elif i == '(':
                s.append(False)
            else:
                if s and word[idx-1] not in ['{','[']:
                    s.pop()
                else:
                    return False
        
        # 올바른 괄호라면 위의 배열에 아무값도 없어야한다.
        return True if len(s+m+l) == 0 else False
    
    s = deque([i for i in s])
    result = 0
    # 주어진 문자열을 큐로 바꾸고 로테이트하면서 확인
    for _ in range(len(s)):
        word = ''.join(s)
        result += 1 if check(word) else 0
        s.rotate(-1)
    
    return result
        