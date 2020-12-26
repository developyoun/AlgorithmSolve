x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

print(max(max(y4,y2)-min(y1,y3), max(x4, x2)-min(x1, x3))**2)