from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # make 3 hashmaps
        # one hashmap is row index -> hashset
        # one hashmap is col index -> hashset
        # last hashmap is tuple (row/3, col/3) -> hashset
        # if a duplicate is found in either sets return false

        # row_map = defaultdict(set)
        # col_map = defaultdict(set)      
        # square_map = defaultdict(set)

        # for r in range(len(board)):
        #     for c in range(len(board[r])):
        #         num = board[r][c]
        #         if num == '.':
        #             continue
        #         if num in row_map[r] or num in col_map[c] or num in square_map[(r//3,c//3)]:
        #             return False
        #         row_map[r].add(num)
        #         col_map[c].add(num)
        #         square_map[(r//3, c//3)].add(num)
        # return True

        hashset = set()
        for r in range(len(board)):
            for num in board[r]:
                if num == '.':
                    continue
                if num in hashset:
                    return False
                hashset.add(num)
            hashset = set()
        
        for c in range(len(board[0])):
            for r in range(len(board)):
                num = board[r][c]
                if num is '.':
                    continue
                if num in hashset:
                    return False
                hashset.add(num)
            hashset = set()

        square = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[r])):
                num = board[r][c]
                if num == '.':
                    continue
                if num in square[(r//3,c//3)]:
                    return False
                square[(r//3,c//3)].add(num)
        return True























