def calc(k, n):
    cnt = 0
    while k:
        k //= n
        cnt += k
    return cnt

n, m = list(map(int, input().split()))
print(min(calc(n, 5) - calc(m, 5) - calc(n-m, 5), calc(n, 2)- calc(m, 2)-calc(n-m, 2)))