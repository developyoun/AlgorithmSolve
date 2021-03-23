from itertools import permutations
def solution(numbers):
    answer = 0
    s = set()
    for n in range(1, len(numbers)+1):
        for perm in permutations(numbers, n):
            s.add(int(''.join(perm)))
    
    for num in s:
        if not num % 2 or num == 1:
            if num == 2:
                answer += 1
        else:
            for i in range(3, int(num**0.5)+1, 2):
                if not num % i: break
            else:
                answer += 1
                print(num)
    print(s, answer)
    return answer

solution("1777")