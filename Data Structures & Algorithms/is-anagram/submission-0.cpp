class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size())
        {
            return false;
        }
        vector<int> markers(26,0);
        for(size_t i = 0; i < s.size(); i++)
        {
            markers[s[i] - 'a']++;
        }
        for(size_t j = 0; j < t.size(); j++)
        {
            if(markers[t[j] - 'a'] == 0)
                return false;
            markers[t[j] - 'a']--;
        }
        return true;
    }
};
