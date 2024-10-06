class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def rec_check(met, row, col, visited) -> bool:

            #isnt part of the solution or was visited already
            if not word.startswith(met + board[row][col]) or (row, col) in visited:
                return False
            #found the word.
            if met + board[row][col] == word:
                return True
            
            visited.add((row,col))

            #down
            if row + 1 < len(board) and rec_check(met + board[row][col], row + 1, col, visited):
                return True
            #up
            if row - 1 >= 0 and rec_check(met + board[row][col], row - 1, col, visited):
                return True
            #right
            if col + 1 < len(board[0]) and rec_check(met + board[row][col], row, col + 1, visited):
                return True
            #left
            if col - 1 >= 0 and rec_check(met + board[row][col], row, col - 1, visited):
                return True

            visited.remove((row, col))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if rec_check('', i,j, set()):
                    return True
        return False
