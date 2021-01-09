for _ in range(int(input())):
    stack = []

    string = list(input())

    result = 0
    what = 0
    for s in string:
        if s == '(':
            result += 1
        elif s == ')':
            result -= 1 
            if result < 0:
                if what > 0:
                    what -= 1
                    result += 1
                # else:
                #     break
        else:
            what += 1

    val = what - result
    if string[0] != ')' and string[-1] != '(' and val >= 0 and not val & 1 and result >= 0:
        print('YES')
    else:
        print('NO')