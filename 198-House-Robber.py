class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        memo = [0 for _ in range(len(nums))]
        memo[0] = nums[0]
        memo[1] = max(memo[0], nums[1])

        for i in range(2, len(nums)):
            memo[i] = max(memo[i-2] + nums[i], memo[i-1])

        return memo[len(nums) - 1]