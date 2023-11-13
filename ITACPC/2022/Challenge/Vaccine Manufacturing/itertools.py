import itertools

n = int(input())

x = []
for i in range(0, n):
    x += input()

x = [''.join(list(x)) for x in itertools.product(x, repeat=n)]

tot = 0

for e in x:
    if e==e[::-1]:
        tot+=1

print(tot % 1_000_000_007)