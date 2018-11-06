n,v = map(float,input().split())
n = int(n)
l = []
acc = []
d = []

for i in range(n):
    tmp1,tmp2,tmp3 = map(float,input().split())
    l.append(tmp1)
    acc.append(tmp2)
    d.append(tmp3)


def minlen(acc1,acc2,d,v):
    t1 =  v / acc1
    len1 = 0.5*acc1*(t1**2)
    t2 = v/acc2
    len2 = 0.5*acc2*(t2**2) + v*d2
    return len2 - len1

res = sum(l)
d2 = 0.0
for i in range(n-1):
    acc1 = acc[i]
    acc2 = acc[i+1]
    d2 = d2 + d[i+1]
    res += minlen(acc1,acc2,d2,v)
print('%.3f'%res)


