class Solution:
    def trap(self, height: List[int]) -> int:

        # it makes sense when u think of each index as a bucket
        # that is bounded by the minimum height between the max of left & right
        # optimal:

        leftMax = height[0]
        rightMax = height[-1]
        l = 0
        r = len(height) - 1
        tot = 0
        while l < r:

            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                tot += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                tot += rightMax - height[r]
            
        return tot
        