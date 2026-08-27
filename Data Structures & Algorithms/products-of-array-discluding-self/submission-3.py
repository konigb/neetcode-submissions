class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # make use of two arrays 
        # one array is the product of everything to the right of index
        # other array is product of everything to the left of index
        # edge cases product to the right of last index is 1, and product to the left of first index is 1
        # finally combine the products of right and left at each index for product of entire list excluding that index
        left_prod = [0] * len(nums)
        right_prod = [0] * len(nums)
        prod = 1
        for i in range(len(nums)): # go left to right
            left_prod[i] = prod
            prod *= nums[i]
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            right_prod[i] = prod
            prod *= nums[i]
        final_prod = [0] * len(nums)
        for i in range(len(nums)):
            final_prod[i] = left_prod[i] * right_prod[i]
        return final_prod
        


        