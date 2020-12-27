r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
if r >= 8:
    print('satisfactory')
else:
    print('unsatisfactory')