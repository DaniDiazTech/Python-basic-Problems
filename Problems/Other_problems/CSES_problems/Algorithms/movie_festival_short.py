s=[[int(i) for i in input().split()] for _ in range(int(input()))]
s.sort(key=lambda x:x[1])
c=m=0
for i, j in s:
    if i >= c:
        m += 1
        c = j
print(m)