class Solution:
    """Solution to problem found at: [https://leetcode.com/problems/add-two-numbers/]
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Create new listnode
        # iterate over listnodes, add digits
            #if >10 carry 1 to next
        # add number to new list node
        #return listnode
        
        ttls = []
        
        carryover = 0
        
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            ttl = l1.val + l2.val + carryover
            
            if ttl >= 10:
                carryover = 1
                ttl -= 10
                if not l1.next:
                    l1.next = ListNode(0)
                if not l2.next:
                    l2.next = ListNode(0)
            else:
                carryover = 0
            ttls.append(ListNode(ttl))
            
            l1 = l1.next
            l2 = l2.next
            
        l3 = ttls[0]
        for index in range(len(ttls) - 1):
            ttls[index].next = ttls[index + 1]
            
        return l3
            
            
                