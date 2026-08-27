class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        res = nums[0]

        while l <= r:

            m = (l + r)//2 

            res = min(res, nums[m])

            if nums[m] > nums[len(nums)-1]:
                l = m + 1
            else:
                r = m - 1

        return res
