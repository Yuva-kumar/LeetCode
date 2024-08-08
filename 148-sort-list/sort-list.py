# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:return head
        l=[]
        temp=head
        while (temp):
            l.append(temp.val)
            temp=temp.next
        l.sort()
        res=ListNode(l[0])
        dup=res
        for i in range(1,len(l)):
            res.next=ListNode(l[i])
            res=res.next
        return dup
        