class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    res.append([nums[i] , nums[j] , nums[k]])
                    j += 1
                    k -= 1

                    # only need to guarantee j is not duplicate to have unique sum
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res