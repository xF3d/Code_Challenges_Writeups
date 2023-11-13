from collections_extended import bag
#TODO find implementation of a good multiset or ask chatgbt

n = int(input())

x = []
for i in range(0, n):
    x.append(input())

#per definizione il primer deve essere fatto di max 2 elementi di x
primer = []
for i in range(0, n):
    for j in range(0, n):
        element = x[i] + x[j]
        if element==element[::-1]:
            primer.append([element, [len(x[i])]])

ls = bag(primer)
temp = bag()
size = 2
count = 0
while size!=n:
    add = 0
    temp = bag()
    for p in ls:
        for i in x:
            for damn in p[1]:
                st = p[0][:damn]
                ed = p[0][damn:]
                
                string = st + i + ed
                if string==string[::-1]:
                    g = temp.count(p[0])
                    total = p[1].copy()
                    total.append(len(st+i))
                    total.append(len(st))
                    temp.append([string, total]*g)
                    add = 1
                    if size+add==n:
                        count+=1*g
    size+=add
    ls = temp

print(temp)
print(count % 1_000_000_007)