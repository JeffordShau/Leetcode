class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0, 0
        len1, len2 = len(word1), len(word2)
        res = []
        while ptr1 < len1 and ptr2 < len2:
            res.append(word1[ptr1])
            res.append(word2[ptr2])
            ptr1 += 1
            ptr2 += 1

        if ptr1 == len1 and ptr2 == len2:
            return ''.join(res)
        elif ptr1 == len1:
            res.append(word2[ptr2:])
            return  ''.join(res)
        elif ptr2 == len2:
            res.append(word1[ptr1:])
            return  ''.join(res)
