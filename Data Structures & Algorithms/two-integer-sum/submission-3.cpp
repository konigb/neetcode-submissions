#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,size_t> map;
        for(size_t i = 0; i < nums.size(); i++)
        {
            map[nums[i]] = i;
        }
        int diff;
        int i,j;
        for(size_t k = 0; k < nums.size(); k++)
        {
            diff = target - nums[k];
            if(map.find(diff) != map.end())
            {
                i = k;
                j = map[diff];
                if(i != j)
                    break;
            }
        }

        vector<int> res(2);
        res[0] = i;
        res[1] = j;
        return res;
    }
};
