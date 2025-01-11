class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(int)
        for idx, num in enumerate(nums):
            complement = target - num
            if complement not in hashMap:
                hashMap[num] = idx
            else:
                return (idx, hashMap[complement])