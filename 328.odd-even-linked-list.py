#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next==None: return head
        odd=ListNode(head.val)
        curr_odd=odd
        even=ListNode(head.next.val)
        curr_even=even
        i=3
        curr=head.next.next
        while curr != None:
            if i %2 !=0 :
                curr_odd.next=ListNode(curr.val)
                curr_odd=curr_odd.next
            else:
                curr_even.next=ListNode(curr.val)
                curr_even=curr_even.next
            curr=curr.next
            i+=1
        curr_odd.next=even
        return odd    
# @lc code=end

