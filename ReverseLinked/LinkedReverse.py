# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Type: Time O(n) Memory O(1)

class Solution(object):
    def reverseList(self, head):
        # We initialize our pointers with prev = none and current = head to start at
        prev = None
        current = head
        # We use this while loop to keep going until current reaches the end of the list
        while current:
            # We create a temporary variable to save current.next so when current.next updates we still have that nextNode pointer
            nextNode = current.next
            # We reverse the pointers by setting current.next = prev
            current.next = prev
            # Updating the previous and setting it to our current 
            prev = current
            # Updating current with the nextNode which is set to the current.next value
            current = nextNode
        return prev