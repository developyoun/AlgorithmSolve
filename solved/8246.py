r, c, w = map(int, input().split())
print((r//w)*(c//w)-max(0, r//w-2)*max(0, c//w-2))
