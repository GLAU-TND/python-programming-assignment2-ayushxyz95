l = eval(input())
n = len(l)
l1 = []
l1.append(l[0])
s = l[0]
for i in range(0,n):
    for j in range(1,n):
        s1 = l[j]
        p = len(s)
        if s[p-1] == s1[0]:
            l1.append(l[j])
            s = s1
            l[j] = '*&'
            break
print(l1)