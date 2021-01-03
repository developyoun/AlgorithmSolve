N = int(input())
arr = input().split()

last = arr.pop()[-1]

while arr:
    flag = False
    for a in arr:
        if last == a[0]:
            last = a[0] 
            arr.remove(a)
            break
    else: flag = True
    
    if flag: break

print(0 if arr else 1)
