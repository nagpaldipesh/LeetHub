# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorderTraversalRecursive(node: Optional[TreeNode], nodes : List[int]):

            if node is None:
                return
            
            nodes.append(node.val)
            preorderTraversalRecursive(node.left, nodes)
            preorderTraversalRecursive(node.right, nodes)

        result = []

        preorderTraversalRecursive(root, result)
        return result
