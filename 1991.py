def dfs(node):

    preorder.append(node)

    new1, new2 = dic[node]
    if new1 != -1:
        dfs(new1)

    inorder.append(node)

    if new2 != -1:
        dfs(new2)

    postorder.append(node)


N = int(input())
dic = {chr(65+i): [-1, -1] for i in range(26)}
for _ in range(N):
    a, b, c = input().split()
    if b != '.':
        dic[a][0] = b
    if c != '.':
        dic[a][1] = c

preorder = []
inorder = []
postorder = []
dfs('A')
print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))
