class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Need pointer i and j
        # Will need nested loop
        # out loop keeps going while i < len(s)
        # make a set in inner loop 
        # inner loop goes form j = i to j < len(s) and no duplicate
        # record size of substring
        # if j = len(s) then break 

        i = 0
        j = i
        res = 0
        
        sub = set()
        while j < len(s):

            c_j = s[j]
            if c_j not in sub:
                sub.add(c_j)
                j += 1
            else:
                res = max(res, len(sub))

                # do some cleaning up
                c_i = s[i]
                while c_i != c_j and i < j:
                    sub.discard(c_i)
                    i += 1
                    c_i = s[i]
                sub.discard(c_i)
                i += 1
        res = max(res, len(sub))
        return res





