class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        subset = []
        def backtrack(idx, sums):
            if sums == target:
                res.append(subset[:])
                return
            elif sums > target:
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                backtrack(i + 1, sums + candidates[i])
                subset.pop()

        backtrack(0, 0)
        return res