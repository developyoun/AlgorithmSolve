p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())

if [p1, p2] == [s2, s1]:
    print("Penalty")
elif p1+p2 == s1+s2:
    print('Persepolis' if s1 < p2 else 'Esteghlal')
else:
    print('Esteghlal' if p1+p2 < s1+s2 else 'Persepolis')