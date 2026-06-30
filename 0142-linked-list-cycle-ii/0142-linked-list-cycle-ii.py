# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        x=0
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                x=1
                break
        if(x):
            fast=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
                
            return fast
        return None
            
           
            

        