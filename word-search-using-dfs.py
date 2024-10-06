class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, index) -> bool:
            if index == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
                return False

            # emptying out letters we vivsited on board
            letter = board[row][col]
            board[row][col] = ''

            if dfs(row+1, col, index+1) or dfs(row-1, col, index+1) or dfs(row, col+1, index+1) or dfs(row, col-1, index+1):
                return True

            board[row][col] = letter

            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
