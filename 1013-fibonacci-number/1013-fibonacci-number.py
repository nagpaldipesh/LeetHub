class Solution:
    memo = {0: 0, 1: 1}

    def fib(self, n: int) -> int:

        if n in self.memo:
            return self.memo[n]

        result = self.fib(n - 1) + self.fib(n - 2)

        self.memo[n] = result

        return result