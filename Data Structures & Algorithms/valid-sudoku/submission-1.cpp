#include <iostream>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int height = 0;
        int width = 0;
        map<int, set<int>> checkRows;
        map<int, set<int>> checkCols;
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
                        {
                            cout << "check3x3 failed" << endl;
                            cout << "row: " << r << endl;
                            cout << "col: " << c << endl; 
                            return false;
                        }
                        if(checkRows[value].find(r) != checkRows[value].end())
                        {
                            cout << "checkRows failed" << endl;
                            cout << "row: " << r << endl;
                            cout << "col: " << c << endl;
                            return false; 
                        }
                        if(checkCols[value].find(c) != checkCols[value].end())
                        {
                            cout << "checkCols failed" << endl;
                            cout << "row: " << r << endl;
                            cout << "col: " << c << endl;
                            return false;
                        }
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
