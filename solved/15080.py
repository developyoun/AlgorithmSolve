arr1 = input().split()
arr2 = input().split()

h, m, s = int(arr2[0])-int(arr1[0]), int(arr2[2])-int(arr1[2]), int(arr2[-1])-int(arr1[-1])

if s < 0:
    s += 60
    m -= 1
if m < 0:
    m += 60
    h -= 1
if h < 0:
    h += 24
print(h*3600 + m*60 + s)