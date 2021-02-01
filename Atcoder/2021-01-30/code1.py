A, B, C = map(int, input().split())

if C:
    if A < B: print('Aoki')
    else: print('Takahashi')
else:
    if A > B: print('Takahashi')
    else: print('Aoki')