class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        clean_s = "".join(lower_s.split(" "))

        # use two pointers
        # one at each end comparing one at a time
        left = 0
        right = len(clean_s) - 1 
        while left < right:
            if not clean_s[left].isalnum():
                left += 1
                continue
            if not clean_s[right].isalnum():
                right -= 1
                continue
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        return True
