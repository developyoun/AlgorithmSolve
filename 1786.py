import sys
input = sys.stdin.readline

def get_pi(string):
    arr = [0] * len(string)
    
    j = 0
    for i in range(1, len(string)):
        while j > 0 and string[i] != string[j]:
            j = arr[j-1]
        if string[i] == string[j]:
            j += 1
            arr[i] = j
    return arr

def search_string(target, arr):

    answer_cnt, answer_idx = 0, []
    idx, k = 0, 0
    while idx <= len(target) - len(arr):

        if k < len(arr) and target[idx+k] == arr[k]:
            k += 1
            if k == len(arr):
                answer_cnt += 1
                answer_idx.append(idx+1)
        else:
            if not k:
                idx += 1
            else:
                idx += k-pi[k-1]
                k = pi[k-1]
    print(answer_cnt)
    print(*answer_idx)

T = input().rstrip()
P = input().rstrip()
pi = get_pi(P)
search_string(T, P)