for _ in range(int(input())):
    N = int(input())
    string = input()

    answer = 'YES' if string == '2020' else 'NO'

    diff = N-4
    for i in range(5):
        left, right = string[:i], string[diff+i:]
        if left+right == '2020':
            answer = 'YES'; break
    print(answer)