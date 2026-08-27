#include <unordered_map>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mymap;
        for(int i = 0; i < nums.size(); i++)
        {
            mymap[nums[i]]+= 1;
        }
        vector<vector<int>> res(nums.size()+1);
        for(auto &pair : mymap)
        {
            res[pair.second].push_back(pair.first);
        }
        vector<int> ans;
        for(int j = res.size()-1; j > 0; j--)
        {
            if(k == 0)
                break;
            if(res[j].size() != 0)
            {
                for(int m = 0; m < res[j].size(); m++ )
                {
                    if(k == 0)
                        break;
                    ans.push_back(res[j][m]);
                    k--;
                }
            }
        }
        return ans;
    }
};
