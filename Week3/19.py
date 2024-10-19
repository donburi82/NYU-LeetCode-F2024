# 19. Remove Nth Node From End of List
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # find the length
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    
    # locate the node to remove
    cnt = length-n
    prev, cur = None, head
    while cnt>0:
        cnt -= 1
        prev = cur
        cur = cur.next

    # remove the node and update
    if prev is None:
        return head.next
    
    next_n = cur.next
    cur = None
    prev.next = next_n
    
    return head

# "single pass"
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # handle edge case (removing the head node)
    dummy = ListNode(0, head)

    # locate the node to remove
    slow = dummy
    fast = dummy
    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    # remove the node and update
    to_remove = slow.next
    slow.next = slow.next.next
    to_remove = None
    
    return dummy.next