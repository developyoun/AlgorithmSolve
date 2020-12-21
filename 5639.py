from collections import deque
import sys

input = sys.stdin.readline
nodes = deque()

while True:
    num = input().rstrip()
    if num == '': break
    nodes.append(int(num))
