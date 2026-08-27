class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet;
        int longest = 0;
        for(int num : nums)
            numSet.insert(num);

        for(auto num : numSet)
        {
            if( numSet.count(num-1) == 0 )
            {
                int length = 1;
                while( numSet.count(num + length) > 0)
                {
                    length += 1;
                }
                longest = max(length, longest);
            }
        }
        return longest;
    }
};
