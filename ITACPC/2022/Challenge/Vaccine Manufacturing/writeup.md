# Vaccine Manufacturing (INCOMPLETE)

Description [here](https://itacpc22.kattis.com/contests/itacpc22/problems/itacpc22.vaccinemanufacturing?tab=metadata).

### Approach 1 (Bruteforce)

To solve this problem we need to use permutations with repetitions, the `itertools` library will be useful in this: 

We can get permutations with no repetition using `itertools.permutations` to get permutations with repetition we need to use `itertools.product` and set repeat to `n`, need the latter.

The solution works but it has an O(n^n) complexity, I need to find a better solution.