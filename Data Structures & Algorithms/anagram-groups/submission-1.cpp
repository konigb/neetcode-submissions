#include <unordered_map>
using namespace std;

class Solution {
public:

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for(int i = 0; i < strs.size(); i++)
        {
            string word = strs[i];
            sort(word.begin(), word.end());
            map[word].emplace_back(strs[i]);
        }
        vector<vector<string>> res;
        for(auto &pair : map)
        {
            res.emplace_back(pair.second);
        }
        return res;
    }
};
