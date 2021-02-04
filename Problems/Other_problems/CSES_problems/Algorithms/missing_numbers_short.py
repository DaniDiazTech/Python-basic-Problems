l = input
s = int
n = s(l())
m = [s(i) for i in input().split()]
print(s((n * (n + 1) / 2) - sum(m)))