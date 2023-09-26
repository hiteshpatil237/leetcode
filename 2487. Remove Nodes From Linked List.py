# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack = []
        temp = head

        while temp:
            while stack and stack[-1].val < temp.val:
                stack.pop()

            if stack:
                stack[-1].next = temp
            else:
                head = temp

            stack.append(temp)
            temp = temp.next
        
        return head