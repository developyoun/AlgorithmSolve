for _ in range(int(input())):
    num = int(input())
 
    while True:

        now = num
        while now:
            rest = now % 10
            now //= 10
            if not rest: continue
            if num % rest: break

        else:
            break
        num += 1
    print(num)