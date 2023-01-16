# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return head
        
        pivot = head.val
        start = head
        
        while head:
            pivot = head.val
            if head.next == None:break
            if pivot == head.next.val:
                head.next = head.next.next                
            else:
                head = head.next
                
            
                
        
        return start
        