# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = []
        temp1, temp2 = [], []
        
        node1, node2 = p, q
        
        while node1 or stack:
            if node1:
                stack.append(node1)
                temp1.append(node1.val)
                node1 = node1.left
            else:
                temp1.append(None)
                node1 = stack.pop()
                node1 = node1.right
        
        
        while node2 or stack:
            if node2:
                stack.append(node2)
                temp2.append(node2.val)
                node2 = node2.left
            else:
                temp2.append(None)
                node2 = stack.pop()
                node2 = node2.right
        
        return temp1 == temp2
            
            