class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def fib(n):
            if n == 0:
                return n
            if n == 1 or n == 2:
                return 1
            if n not in memo:
                memo[n] = fib(n-1) + fib(n-2) + fib(n-3)

            return memo[n]
        return fib(n)