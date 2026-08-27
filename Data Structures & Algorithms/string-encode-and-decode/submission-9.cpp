#include <iostream>

class Solution {
public:

    string encode(vector<string>& strs) {
        if(strs.size() == 0)
            return "empty";
        int len;
        string sol = "";
        for(int i = 0; i < strs.size(); i++)
        {
            len = strs[i].size();
            sol += std::to_string(len) + "#" + strs[i];
        }
        return sol;

    }

    vector<string> decode(string s) {
        if(s == "empty")
            return {};
        vector<string> res;
        string len = "";
        int sLen = 0;
        while(sLen != s.size())
        {
            if(s[sLen] != '#')
            {
                len += s[sLen];
                sLen++;
            }
            if(s[sLen] == '#')
            {
                sLen++;
                string copy = s.substr(sLen, std::stoi(len));
                res.push_back(copy);
                sLen += std::stoi(len);
                len = "";
            }
        }
        return res;

    }
};
