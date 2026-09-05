class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        j = i
        sub = set()
        res = 0

        for j in range(len(s)):

            while s[j] in sub:
                sub.remove(s[i])
                i += 1
            

            sub.add(s[j])

            res = max(res, len(sub))


        return res
        