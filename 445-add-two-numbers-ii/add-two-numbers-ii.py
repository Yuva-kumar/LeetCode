# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=l1
        temp2=l2
        a,b=[],[]
        while temp1:
            a.append(temp1.val)
            temp1=temp1.next
        while temp2:
            b.append(temp2.val)
            temp2=temp2.next
        if len(a)!=len(b):
            x=min(len(a),len(b))
            if x==len(b):
                b=[0]*(len(a)-x)+b
            else:
                a=[0]*(len(b)-x)+a
        res=[]
        c=0
        for i in range(len(a)-1,-1,-1):
            k=a[i]+b[i]+c
            c=k//10
            s=k%10
            res.append(s)
        if c!=0:res.append(c)
        res=res[::-1]
        dum=ListNode()
        pre=dum
        for i in range(len(res)):
            dum.next=ListNode(res[i])
            dum=dum.next
        return pre.next
        