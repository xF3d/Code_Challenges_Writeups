def xinput():
    s = input()
    s = list(s.split())
    s = [int(i) for i in s]
    return s

N, M, K = xinput()

L = []

def filter(eq, lst):
    out = []
    for x in lst:
        if eq in x:
            e = x[0] if x[1]==eq else x[1]
            out.append(e)
    return out

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

for i in range(0, M):
    a, b = xinput()
    L.append([a, b])

for i in range(1, N):
    iL = filter(i, L)
    jL = []
    
    for j in range(i+1, N+1):
        jL = filter(j, L)
        if(len(intersection(jL, iL))==K):
            print("YES")
            exit()

print("NO")