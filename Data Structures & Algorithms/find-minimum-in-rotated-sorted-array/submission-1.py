class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 1
        r = len(nums)

        res = nums[0]

        while l <= r:

            m = (l + r)//2 % len(nums)

            res = min(res, nums[m])

            if nums[m] > nums[len(nums)-1]:
                l = m + 1
            else:
                r = m - 1
        return res
