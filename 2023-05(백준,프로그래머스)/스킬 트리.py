def solution(skill, skill_trees):
    skill = list(skill)
    
    result = 0
    for st in skill_trees:
        # 스킬 트리를 따라야 하는것만 남긴다.
        st = [i for i in st if i in skill]
        if st == skill[:len(st)]:
            result += 1
    return result
            