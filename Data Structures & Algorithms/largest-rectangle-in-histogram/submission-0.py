class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # as long as height is increaseing include pair of (height, index)
        # if height decreases then calculate area for top value
        # continue to do this and pop values that are less than current
        # once you can not pop anymore change start index to last popped

        stack = []
        max_area = 0
        for i,h in enumerate(heights):
            if len(stack) == 0 or stack[-1][1] <= h:
                stack.append((i,h))
            else:
                start_index = i
                while stack and stack[-1][1] > h:
                    area = stack[-1][1] * (i - stack[-1][0])
                    max_area = max(max_area, area)
                    start_index = stack[-1][0]
                    stack.pop()
                stack.append((start_index, h))
        for i, h in stack:
            l = len(heights) - i
            max_area = max(max_area, h * l)
        return max_area

        