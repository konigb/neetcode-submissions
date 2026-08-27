#include <unordered_set>
using namespace std;
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> myset;
        for(size_t i = 0; i < nums.size(); i++)
        {
            if(myset.find(nums[i]) != myset.end())
            {
                return true;
            }
            myset.insert(nums[i]);
        }
        return false;
    }
};
