class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = deque()
        digits[-1] += 1
        while digits:
            curr = digits.pop()
            if curr == 10:
                if digits:
                    digits[-1] += 1
                else:
                    digits.append(1)
                result.appendleft(0)
            else:
                result.appendleft(curr)
        return list(result)
