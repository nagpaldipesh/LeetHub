# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def postorderTraversalRecursive(node: Optional[TreeNode], nodes: List[int]) -> None:

            if node is None:
                return

            postorderTraversalRecursive(node.left, nodes)
            postorderTraversalRecursive(node.right, nodes)
            nodes.append(node.val)

        result = []
        postorderTraversalRecursive(root, result)
        
        return result