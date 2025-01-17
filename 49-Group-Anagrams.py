class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for chars in strs:
            count = [0] * 26
            for char in chars:
                count[ord(char) - ord('a')] += 1
            freq[tuple(count)].append(chars)
        
        res = []
        for _, val in freq.items():
            res.append(val)

        return res
        
            