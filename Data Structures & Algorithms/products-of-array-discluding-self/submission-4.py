class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # make use of two arrays 
        # one array is the product of everything to the right of index
        # other array is product of everything to the left of index
        # edge cases product to the right of last index is 1, and product to the left of first index is 1
        # finally combine the products of right and left at each index for product of entire list excluding that index
        final_prod = [1] * len(nums)
        prod = 1
        for i in range(len(nums)): # go left to right
            final_prod[i] *= prod
            prod *= nums[i]
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            final_prod[i] *= prod
            prod *= nums[i]
        return final_prod
        


        