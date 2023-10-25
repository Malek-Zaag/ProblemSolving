# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None : 
            return None 
        curr=head
        li=[]
        while curr != None:
            li.append(curr.val)
            curr=curr.next
        new=ListNode(li[-1])
        curr1=new
        for i in range(len(li)-2,-1,-1):
            toAdd=ListNode(li[i])
            curr1.next=toAdd
            curr1=toAdd
        print(new)
        return new