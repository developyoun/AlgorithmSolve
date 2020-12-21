N = int(input())

max_points = [0, 0, 0]
min_points = [0, 0, 0]
for n in range(N):
    numbers = list(map(int, input().split()))    
    
    a = max(max_points[0], max_points[1]) + numbers[0]
    b = max(max_points) + numbers[1]
    c = max(max_points[1], max_points[2]) + numbers[2]
    max_points = [a, b, c]

    a = min(min_points[0], min_points[1]) + numbers[0]
    b = min(min_points) + numbers[1]
    c = min(min_points[1], min_points[2]) + numbers[2]
    min_points = [a, b, c]

print(max(max_points), min(min_points))