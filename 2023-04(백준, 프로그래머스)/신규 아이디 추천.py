def solution(new_id):

    check = set([str(i) for i in range(10)] + ['-','_','.'] + [chr(i) for i in range(97,123)])

    # 1 단계 - 소문자 변환
    new_id = new_id.lower()

    # 2 단계 - 필요없는 문자 삭제 
    new_id = [w for w in new_id if w in check]
    
    # 3 단계 - '.' 연속된거 처리하기
    id = []
    for i in new_id:
        if not id:
            id.append(i)
        elif id[-1] == '.' and i == '.':
            continue
        else:
            id.append(i)
    new_id = id
    
    # 4 단계 - 앞,뒤 '.' 문자 처리하기
    if new_id and new_id[0] == '.':
        new_id.pop(0)
    if new_id and new_id[-1] == '.':
        new_id.pop()
    
    # 5 단계 - 빈문자열 처리하기
    if not new_id:
        new_id = ['a']

    # 6 단계 - 16자 넘는거 처리하기
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id.pop()

    # 7 단계 - 2자 이하인거 처리하기
    if len(new_id) <= 2:
        new_id += [new_id[-1]] * (3-len(new_id))
    
    return ''.join(new_id)
    