def solution(genres, plays):
    answer = []
    dic = dict()
    cnt = dict()
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        try:
            dic[genre].append([play, i])
            cnt[genre] += play
        except:
            dic[genre] = [[play, i]]
            cnt[genre] = play
    
    for li in dic.values():
        li.sort(key=lambda x:(-x[0], x[1]))
    arr = sorted(list(cnt.items()), key=lambda x:-x[1])

    for g, t in arr:
        answer.append(dic[g][0][1])
        if len(dic[g]) >= 2:
            answer.append(dic[g][1][1])
    return answer