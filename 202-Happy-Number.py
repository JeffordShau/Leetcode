class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while True:
            sums = 0
            while n > 9:
                sums += pow(n % 10, 2)
                n = n // 10
            sums += pow(n, 2)
            if sums == 1:
                return True
            elif sums in nums:
                return False
            else:
                n = sums
                nums.add(sums)
