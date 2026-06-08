# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # ダミーノードを作成
        tail = dummy  # tailはダミーノードから開始
        if not list1 and not list2:
            return None     
        while list1 and list2:   
            if list1.val<=list2.val:
                tmp=ListNode(list1.val)
                tail.next=tmp
                list1=list1.next
            else:
                tmp=ListNode(list2.val)
                tail.next=tmp
                list2=list2.next
            tail=tail.next
        if list1:
            tail.next=list1
        else:
            tail.next=list2
        return dummy.next