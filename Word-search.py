class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def rec_check(met, row, col):
            if met.join(board[row][col]) not in word:
                return
                ##make copy of board. to avoid going over the same place twice, erase values at cells after making sure that some value is in the word. the copy should restart when we return and in the meantime we erased.  maybe be a passable attribute?DEF. 
            #up
            try:
               a=board[row+1, col]
            except:
                pass
            else:
                rec_check(met.join(board[row][col]), row+1, col)
            #down
            try:
               a=board[row-1, col]
            except:
                pass
            else:
                rec_check(met.join(board[row][col]), row-1, col)
            #right
            try:
               a=board[row, col+1]
            except:
                pass
            else:
                rec_check(met.join(board[row][col]), row, col+1)
            #left
            try:
               a=board[row, col-1]
            except:
                pass
            else:
                rec_check(met.join(board[row][col]), row, col-1)

            return met


        for i in range(len(board)-len(word)):
            for j in range(len(board[0])-len(word))
                met=''
                if rec_check(met, i,j) == word:
                    return True
        return False

            
