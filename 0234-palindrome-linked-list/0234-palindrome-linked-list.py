class Solution:
    

    def isPalindrome(self, head):

        # If list has 0 or 1 node
        if not head or not head.next:
            return True

        # Step 1: Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second_half = self.reverse(slow)

        # Step 3: Compare first half and second half
        first_half = head

        while second_half:
            if first_half.val != second_half.val:
                return False

            first_half = first_half.next
            second_half = second_half.next

        return True
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev