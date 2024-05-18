#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=self.getLength(head)
        if (length==1 or length==0): return None
        curr=head
        i=0
        while(i < length//2 -1):
            i+=1
            curr=curr.next
        curr.next=curr.next.next
        print(i)
        return head
        
        
    def getLength(self,head):
        length=0
        curr=head
        while curr != None:
            curr =curr.next
            length+=1
        return length        
# @lc code=end

