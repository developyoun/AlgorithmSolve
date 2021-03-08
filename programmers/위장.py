def solution(clothes):
    dic = {}
    for v, k in clothes:
        try:
            dic[k].append(v)
        except:
            dic[k] = [v]
    
    answer = 1
    for v in dic.values():
        answer *= len(v)+1
    return answer - 1 
