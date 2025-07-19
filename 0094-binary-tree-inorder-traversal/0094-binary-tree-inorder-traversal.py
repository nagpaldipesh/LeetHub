# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorderTraversal(node : Optional[TreeNode], nodes: List[int]):
            if node is None:
                return
            
            inorderTraversal(node.left, nodes)
            nodes.append(node.val)
            inorderTraversal(node.right, nodes)
            

        result = []
        inorderTraversal(root, result)

        return result

