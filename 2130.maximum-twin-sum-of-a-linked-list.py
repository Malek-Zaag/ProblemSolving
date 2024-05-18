#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head == None : return 0
        if head.next == None: return head.val
        r=self.getToEnd(head)
        l=0
        li=[]
        curr=head
        while curr != None:
            li.append(curr.val)
            curr=curr.next
        l=0
        maxi=0
        while l < r:
            maxi=max(li[l]+li[r],maxi)
            l+=1
            r-=1
        return maxi

    def getToEnd(self,head):
        i=0
        curr=head
        while curr.next != None:
            i+=1
            curr=curr.next
        return i
        
        
# @lc code=end

