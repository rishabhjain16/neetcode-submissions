# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        def conquer(l1,l2):
            dummy = ListNode(0)
            current = dummy
            while l1 and l2:
                if l1.val<l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2=l2.next
                current=current.next
            current.next = l1 or l2
            return dummy.next
        def divide(lists, l,r):
            if l>r:
                return None
            if l==r:
                return lists[l]
            mid = (l+r)//2
            left = divide(lists,l,mid)
            right = divide(lists, mid+1, r)
            return conquer(left,right)
        
        return divide(lists,0,len(lists)-1)


        


        