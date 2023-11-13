import itertools

n = int(input())

x = []
for i in range(0, n):
    x += input()

x = [e for x in itertools.product(x, repeat=n) if (e := ''.join(x)) == e[::-1]]
print(len(x))