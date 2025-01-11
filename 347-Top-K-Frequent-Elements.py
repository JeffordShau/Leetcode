class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        nums = list(set(nums))

        k = len(nums) - k

        def quicksort(l, r):
            p = l
            for i in range(l, r):
                if counter[nums[i]] <= counter[nums[r]]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p == k:
                print(nums)
                res = []
                for i in range(k, len(nums)):
                    res.append(nums[i])
                return res
            elif p < k:
                return quicksort(p + 1, r)
            else:
                return quicksort(l, p - 1)
        
        return quicksort(0, len(nums) - 1)