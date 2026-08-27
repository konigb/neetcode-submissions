from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # use a hashmap to aggregate

        # iterate over hashmap adding each key,value as tuples in list

        # sort list by the frequency of each tuple

        # get the top k 

        # Time complexity is O(nlogn)
        
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        res = []
        for j,v in hashmap.items():
            res.append((j,v))
        res = sorted(res, key=lambda freq: freq[1], reverse=True)
        
        fin_res = []
        for i in range(0,k):
            fin_res.append(res[i][0])

        return fin_res
