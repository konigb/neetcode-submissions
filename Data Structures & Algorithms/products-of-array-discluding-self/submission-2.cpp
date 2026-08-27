class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int pre = 1;
        int suf = 1;
        vector<int> res(nums.size());
        res[0] = pre;
        for(int i = 1; i < nums.size(); i++)
        {
            pre = nums[i-1] * pre;
            res[i] = pre;
        }
        for(int i = nums.size()-2; i >=0; i--)
        {
            suf = nums[i+1] * suf;
            res[i] *= suf;
        }
        return res;

    }
};
