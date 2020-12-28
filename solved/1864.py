dic = {'-':0, "\\":1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1 }

while True:
    string = input()
    if string == '#': break

    result = 0
    n = len(string)
    while n:
        s = string[len(string) - n]
        result += 8**(n-1) * dic[s]

        n -= 1
    print(result)