class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # The most important thing about this problem is finding the start of a sequence
        # Use a set to find the start of a sequence check if num-1 is in the set
        # record all the numbers that start a sequence
        # for each number that starts a sequence count the length by checking num + 1, num + 2, ... etc
        # return the longest sequence

        hashset = set(nums)
        seq_starts = []
        for num in nums:
            if (num-1) not in hashset:
                seq_starts.append(num)
        
        longest_len = 0
        for start in seq_starts:
            curr_len = 1
            while (start+curr_len) in hashset:
                curr_len +=1
            longest_len = max(curr_len, longest_len)
        return longest_len