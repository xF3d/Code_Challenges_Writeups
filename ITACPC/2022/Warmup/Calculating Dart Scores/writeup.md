# Calculating Dart Scores

Description [here](https://itacpc22.kattis.com/contests/wdqnr2/problems/calculatingdartscores).

# Approach 1 (Greedy)

I first try to solve said problem using a greedy algorithm, where I try maximizing the `"triple"` values and then go for `"double"` and last `"single"`, here is the code [greedy.c](./greedy.c). This works, but not for all cases, for instance it won't work for a number like 137 as it will output:

`triple 20
triple 20
triple 5
double 1
Impossible`

Even if it is actually possible to get said number with only 3 lines in this way:

`triple 20
triple 19
double 10`

So this is just only a partial solution to the problem.

# Approach 2 (Dynamic Programming)

Let's break this problem into easier subproblems to solve, I decided to break down the problem as follows:

- When `1 <= n <= 60` we can solve the problem using only singles.
- Any `n > 60` will have a `triple 20`, so we will need to consider only 2 lines, and let's make it easier by considering only `double` and `triple`. This way we can represent any number until `triple 20` and `double 20`.
- If we solve the problem 2, we will lose the solution 61, I will make its own case.
- Any `n > 20*3 + 20*3 + 20*2`, equal to `n > 160` will necessarily have all the 3 lines set to `triple` and as such `n` must be divisible by 3, otherwise we can't obtain such a result.

The second problem is the trickier one, but we can do this easily by making sure that the dividend of 3 and `n` are both even or both odd, this way we can divide by 2 after that. The result is [code.c](./code.c). If we try pasting 137 we can see that the result is correct.