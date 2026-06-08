# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=head
        stack=[]
        while n:
            stack.append(n.val)
            n=n.next
        n=head
        while stack:
            n.val=stack.pop()
            n=n.next
        return head




        