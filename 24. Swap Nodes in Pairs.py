# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper( node ):
            if not node or not node.next:
                return node

            next_node = node.next
            next_pair = next_node.next

            next_node.next = node

            node.next = helper(next_pair)

            return next_node

        return helper(head)