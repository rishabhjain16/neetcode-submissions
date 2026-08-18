# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        l = 0

        count=0
        while current:
            l+=1
            current = current.next
        x = l-n
        if x==0:
            return head.next
        current = head
        count = 0
        while current:
            count+=1
            if count==x:
                current.next=current.next.next
                break
            current = current.next
        return head

        