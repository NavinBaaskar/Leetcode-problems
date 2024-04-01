memo = [None] * 100


def fib(n: int) -> int:
    if memo[n] is not None:
        return memo[n]
    if n == 1:
        return 1
    if n == 0:
        return 0

    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


print(fib(6))
