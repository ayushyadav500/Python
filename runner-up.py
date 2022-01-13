n = input()
A = []
A = list(map(int,input().split()))
A = sorted(A)
s = set(A)
s.remove(max(s))
print(max(s))
