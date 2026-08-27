class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int comp = 1;
        int incomp = 1;
        int index = -1;
        for(int i = 0; i < nums.size(); i++)
        {
            comp *= nums[i];
            if(nums[i] == 0 && index == -1)
                index = i;
            if(i != index)
                incomp *= nums[i];
        }
        vector<int> res(nums.size());
        for(int j = 0; j < nums.size(); j++)
        {
            if(nums[j] != 0)
                res[j] = comp/nums[j];
            else
                res[j] = incomp;
        }
        return res;
    }
};
