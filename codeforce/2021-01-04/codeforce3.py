for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = [0] * N

    result = 0
    for i in range(N):
        if answer[i]: continue
        answer[i] = arr[i]

        idx = i
        while idx+arr[idx] < N and answer[idx+arr[idx]] < answer[idx] + arr[idx+arr[idx]]:
            answer[idx+arr[idx]] = answer[idx] + arr[idx+arr[idx]]
            idx += arr[idx]
    print(max(answer))