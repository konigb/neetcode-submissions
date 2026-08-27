class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # create a hashmap 
        # iterate through list of numbers and at each index map int to index
        # if i is less than j, then as i approaches j, i will be a value we recorded in the past
        # when a match is found return an ordered list

        hashmap = dict()

        for i in range(0,len(nums)):
            res = target - nums[i]

            if hashmap.get(res) != None:
                return [hashmap[res], i]
            
            if hashmap.get(nums[i]) == None: # want the smallest index so if duplicates ignore later values
                hashmap[nums[i]] = i
        