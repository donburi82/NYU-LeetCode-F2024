# 234. Palindrome Linked List
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # find the middle
    slow = head
    fast = head
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    # reverse the second half
    prev, cur = None, slow
    while cur:
        next_n = cur.next
        cur.next = prev
        prev = cur
        cur = next_n

    # compare two pointers
    while head and prev:
        if head.val!=prev.val:
            return False
        head = head.next
        prev = prev.next
    
    return True