# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import math
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        dup=ListNode()
        res=dup
        while temp.next:
            dup.next=ListNode(temp.val)
            a=math.gcd(temp.val,temp.next.val)
            dup=dup.next
            dup.next=ListNode(a)
            dup=dup.next
            temp=temp.next
        dup.next=ListNode(temp.val)
        return res.next



        