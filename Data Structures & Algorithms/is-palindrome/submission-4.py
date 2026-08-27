class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = s.lower().split(' ')
        newS = "".join(newS)
        start = 0
        end = len(newS) - 1
        while start <= end:
            if not newS[start].isalnum():
                start += 1
            if not newS[end].isalnum():
                end -= 1
            if start <= end and start < len(newS) and newS[start] != newS[end]:
                return False
            start += 1
            end -= 1
        return True

        