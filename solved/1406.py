from collections import deque
import sys
input = sys.stdin.readline

string = input().rstrip()
N = int(input())

left, right = deque(string), deque()
for _ in range(N):
    order = input().split()

    if order[0] == 'P':
        s = order[1]
        left.append(s)
        
    elif order[0] == 'L' and left:
        right.appendleft(left.pop())
    
    elif order[0] == 'D' and right:
        left.append(right.popleft())

    elif order[0] == 'B' and left:
        left.pop()

print(''.join(left) + ''.join(right))