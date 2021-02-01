def checked(string):
    for n in range(2, len(string)//2+1):
        for idx in range(len(string)):
            if string == '1213123132121312' and n == 2:
                print(string[idx:idx+n], string[idx+n:idx+2*n])
            if string[idx:idx+n] == string[idx+n:idx+2*n]:
                return False
    return True

result = '4'*80
def dfs(string, depth):
    global result
    if string >= result: return
    if not checked(string): return

    if depth == N:
        result = min(result, string)
        return
    
    for new in ('1', '2', '3'):
        if string[-1] == new: continue
        dfs(string+new, depth+1)

N = int(input())
s = '1'

dfs(s, 1)
print(result)