# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0  #to count to kth
        self.result = None    #to store result. needed, cause we need to end recursion

        def in_order_travelsal(node):
            if node is None:            #if no further node
                return

            in_order_travelsal(node.left)   #left

            self.count += 1         #what to do with root: here count to k and if its result, store it
            if self.count == k:
                self.result = node.val
                return
 
            in_order_travelsal(node.right)      #right

        in_order_travelsal(root)        #call function from root(that uses class TreeNode)

        return self.result              #return the stored result
