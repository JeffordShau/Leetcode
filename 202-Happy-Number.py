class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while True:
            sums = 0
            while n:
                sums += pow(n % 10, 2)
                n = n // 10
            if sums == 1:
                return True
            elif sums in nums:
                return False
            else:
                n = sums
                nums.add(sums)
