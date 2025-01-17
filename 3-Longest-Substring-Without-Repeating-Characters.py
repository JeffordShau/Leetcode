class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lPtr = 0
        maxLength = 0
        chars = {}
        for rPtr, char in enumerate(s):
            if char in chars and chars[char] >= lPtr:
                lPtr = chars[char] + 1     
            chars[char] = rPtr
            maxLength = max(maxLength, rPtr - lPtr + 1)
        
        return maxLength
            