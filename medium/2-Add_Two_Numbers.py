# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        a,b,carry_over = 0,0,0
        while l1 or l2 or carry_over:
            if l1:
                a=l1.val
                l1 = l1.next
            if l2:
                b=l2.val
                l2 = l2.next
            c = a+b+carry_over
            a,b,carry_over = 0,0,0
            if c>9:
                c = int(str(c)[1])
                carry_over+=1
            dummy = ListNode(c)
            curr.next = dummy
            curr = curr.next
        return res.next