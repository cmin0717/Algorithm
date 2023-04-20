def solution(m, musics):
    
    result, new_m = [],'' 
    m += ' '
    
    # #이 붙은 음은 소문자로 변환하여 표시하기위해 새로운 m을 만들어준다.
    for i in range(len(m)-1):
        if m[i] == '#':continue 
        new_m += m[i].lower() if m[i+1] == '#' else m[i]
    
    for i in musics:
        # 주어진 문자열을 형태에 맞게 잘라준다.
        s,e,title,md = i.split(',')
        s = int(s.split(':')[0]) * 60 + int(s.split(':')[1])
        e = int(e.split(':')[0]) * 60 + int(e.split(':')[1])
        tt = abs(s-e)
        
        # 음표도 #붙은 음표를 따라 처리하기위해 새로운 md를 만들어준다.
        new_md = ''
        md += ' '
        for i in range(len(md)-1):
            if md[i] == '#':continue
            new_md += md[i].lower() if md[i+1] == '#' else md[i]
        
        # 재생된 시간에 맞게 음표의 길이를 확장, 재생시간이 더 적다면 길이에 맞게 축소
        if tt > len(new_md):
            div,mod = divmod(tt, len(new_md))
            new_md = new_md * div + new_md[:mod]
        else:
            new_md = new_md[:tt]

        # 출력 조건에 맞게 처리
        if new_m in new_md:
            if not result:
                result = [tt,title]
            else:
                if result[0] < tt:
                    result = [tt,title]
    
    return result[1] if result else '(None)'
        
        