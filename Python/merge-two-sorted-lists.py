class Solution:
    """Solution to problem found at: [https://leetcode.com/problems/merge-two-sorted-lists/]
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = dummy = ListNode(0)
                
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
                
            dummy = dummy.next
            
        while l1:
            dummy.next = l1
            l1 = l1.next
            dummy = dummy.next
            
        while l2:
            dummy.next = l2
            l2 = l2.next
            dummy = dummy.next
        
        l3 = l3.next
        return l3