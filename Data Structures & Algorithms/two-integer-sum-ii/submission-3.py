class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # use a pointer at both ends
        # if sum total is greater than target then right must move down
        # if sum total is less than target then left must move up

        left = 0
        right = len(numbers)-1
        while left < right:
            tot = numbers[left] + numbers[right]
            if tot > target:
                right -= 1
            elif tot < target:
                left += 1
            else:
                return [left+1, right+1]
            
        