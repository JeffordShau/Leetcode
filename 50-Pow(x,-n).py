class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x: float, n: int) -> float:
            if x == 0:
                return 0
            elif n == 0:
                return 1
            result = helper(x, n // 2)
            result = result * result
            if n % 2 == 0:
                return result
            else: 
                return x * result

        product = helper(x, abs(n))
        if n < 0:
            return 1/product
        else:
            return product