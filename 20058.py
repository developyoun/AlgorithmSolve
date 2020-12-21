def rotate_ice(L):
    new_board = [[0]*(2**N) for _ in range(2**N)]
    for i in range(0, 2**N, 2**L):
        for j in range(0, 2**N, 2**L):
            
            M = 2**L
            for r in range(2**L):
                for c in range(2**L):
                    new_board[i+c][M+j-r-1] = board[i+r][j+c]
            
    return new_board

def melting_ice():

    new_board = [[board[i][j] for j in range(2**N)] for i in range(2**N)]
    for i in range(2**N):
        for j in range(2**N):
            if not board[i][j]: continue

            cnt = 0
            for dy, dx in ((-1, 0), (0, 1), (0, -1), (1, 0)):
                new_y, new_x = i+dy, j+dx
                if 0 <= new_y < 2**N and 0 <= new_x < 2**N and board[new_y][new_x]:
                    cnt += 1

            if cnt < 3:
                new_board[i][j] -= 1
                
    return new_board

def search_big():
    
    best = 0
    visited = [[False]*2**N for _ in range(2**N)]
    for i in range(2**N):
        for j in range(2**N):
            if visited[i][j] or not board[i][j]: continue
            visited[i][j] = True
            cnt = 1
            q = [[i, j]]

            while q:
                y, x = q.pop()

                for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    new_y, new_x = y+dy, x+dx
                    if not 0 <= new_y < 2**N or not 0 <= new_x < 2**N: continue
                    if not visited[new_y][new_x] and board[new_y][new_x]:
                        visited[new_y][new_x] = True
                        cnt += 1
                        q.append([new_y, new_x])

            best = max(best, cnt)

    return best


N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
size = list(map(int, input().split()))

for s in size:
    board = rotate_ice(s)
    board = melting_ice()

result = search_big()

print(sum(map(sum, board)))
print(result)