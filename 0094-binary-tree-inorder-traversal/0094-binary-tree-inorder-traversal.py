# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        stack = []
        
        node = root
        
        while node or stack:
          
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                answer.append(node.val)
                node = node.right
        
        return answer