text = 'a pattern matching algorithm'
pattern = 'rithm'
s = pattern[::-1] # 패턴 문자열을 뒤집어 저장 (보이어 무어는 뒤부터 확인하기 떄문에)
skip = list(range((len(pattern))))
 
i = len(pattern)-1 # 인덱스로 접근 해야하므로 -1
result = 0
 
while i < len(text): # 확인 범위를 주어진 텍스트 보다 멀리간다면 주어진 텍스트에 패턴 문자는 없는것
    nxt = len(s) # 일치하는 문자가 없을경우 더해줄 변수, 초기값은 주어진 패턴문자의 길이로 설정
    j = 0 # 패턴 문자확인 인덱스
    if s[j] == text[i]: # 패턴문자와 주어진 텍스트가 같은 인덱스에 같다면
        while j < len(s): # 앞에 문자들을 확인해 준다.
            if s[j] != text[i-j]: # 현재 패턴 문자를 뒤집어 저장했기에 이렇게 비교해야한다.
                break
            j += 1
        if j == len(s): # 만약 while문을 break없이 나왔다면 전부 같았다는 말이니깐 패턴 문자가 텍스트에 존재
            result = 1
    else:
        while j < len(s): # 다른 글자가 나왔다면 그문자가 패턴 문자에 존재하는지 체크
            if s[j] == text[i]: 
                nxt = min(j, nxt) # 보이어 무어는 뒤에 문자부터 확인하기에 같은 문자가 여러개 존재해도 제일 우측에 있는 문자를 기준
                break
            j += 1
    if result:
        break
    i += nxt # 아까 위에서 구한 nxt만큼 텍스트 문자의 확인 인덱스에 더해주고 다시 확인
 
print(result)