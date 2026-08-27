import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        res = r

        while l <= r:
            k = (l + r)//2

            totHour = 0
            for p in piles:
                totHour += math.ceil(float(p)/k)
            
            if totHour <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res

