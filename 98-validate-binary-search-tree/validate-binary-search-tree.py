# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        res = self.checkBST(root)
        if res is None:
            return True
        for i in range(1,len(res)):
            if res[i-1] < res[i]:
                continue
            else:
                return False
        
        return True
        

    def checkBST(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.checkBST(root.left) + [root.val] + self.checkBST(root.right)
