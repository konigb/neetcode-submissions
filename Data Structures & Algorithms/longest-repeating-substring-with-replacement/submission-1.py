class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        res = 0
        i = 0
        maxf = 0 # Keeps track of the most frequent character count in the current window

        for j in range(len(s)):
            # 1. Add the new character to our frequency map
            count[s[j]] = count.get(s[j], 0) + 1
            
            # 2. Update the highest frequency count
            maxf = max(maxf, count[s[j]])

            # 3. Check if the window is invalid
            # Window length is (j - i + 1). 
            # If the characters we need to replace > k, shrink the window.
            while (j - i + 1) - maxf > k:
                count[s[i]] -= 1
                i += 1
            
            # 4. The window is now guaranteed valid. Update the result.
            res = max(res, j - i + 1)

        return res
        