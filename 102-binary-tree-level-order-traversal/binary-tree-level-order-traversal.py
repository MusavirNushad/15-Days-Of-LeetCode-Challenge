# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            level = []
            size = len(q)

            for _ in range(size):
                Node = q.popleft()
                level.append(Node.val)

                if Node.left:
                    q.append(Node.left)
                if Node.right:
                    q.append(Node.right)
                
            result.append(level)
        
        return result