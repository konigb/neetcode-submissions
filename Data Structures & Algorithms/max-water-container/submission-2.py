class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # The nature of the problem the greatest limiting factor is the height
        # start at opposite ends and calculate area at each interval
        # move the side with the smaller height forward
        # repeat while the left and right do not cross

        area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            water_area = (right - left) * min(heights[left], heights[right])

            area = max(area, water_area)

            if heights[left] <= heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            
        return area