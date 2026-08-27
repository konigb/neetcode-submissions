class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Time complexity O(n) & Space O(n)

        # check size of s & t
        if len(s) != len(t):
            return False
        # make a hashmap for both s and t
        hash_s = dict()
        hash_t = dict()
        # count frequencies and compare
        for l in s:
            if hash_s.get(l,0) == 0:
                hash_s[l] = 1
            else:
                hash_s[l] += 1

        for l in t:
            if hash_t.get(l,0) == 0:
                hash_t[l] = 1
            else:
                hash_t[l] += 1
        
        return hash_s == hash_t
        