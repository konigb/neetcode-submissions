#include <iostream>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int height = 0;
        int width = 0;
        unordered_map<int, unordered_set<int>> checkRows;
        unordered_map<int, unordered_set<int>> checkCols;
        while(height < 9)
        {
            set<int> check3x3;
            for(int r = width; r < width+3; r++)
            {
                for(int c = height; c < height+3; c++)
                {
                    if(board[r][c] != '.')
                    {
                        int value = board[r][c] - '0';
                        if(check3x3.find(value) != check3x3.end())
                            return false;
                        if(checkRows[value].find(r) != checkRows[value].end())
                            return false; 
                        if(checkCols[value].find(c) != checkCols[value].end())
                            return false;
                        check3x3.insert(value);
                        checkRows[value].insert(r);
                        checkCols[value].insert(c);
                    }
                }
            }
            width += 3;
            if(width == 9)
            {
                height += 3;
                width = 0;
            }
        }
        return true;
    }
};
