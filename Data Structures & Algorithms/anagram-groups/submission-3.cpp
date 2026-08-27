#include <unordered_map>
using namespace std;

class Solution {
public:

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for(int i = 0; i < strs.size(); i++)
        {
            int count[26] = {0};
            for(int j = 0 ; j < strs[i].size(); j++)
            {
                count[strs[i][j] - 'a']++;
            }
            string key = "";
            for(int j = 0; j < 26; j++)
            {
                key += std::to_string(count[j]+'a');
            }
            map[key].emplace_back(strs[i]);
        }
        vector<vector<string>> res;
        for(auto &pair : map )
        {
            res.emplace_back(pair.second);
        }
        return res;
    }
};
