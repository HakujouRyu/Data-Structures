class Solution:
    def reverse(self, x: int) -> int:
    """Solution to problem found at: [https://leetcode.com/problems/reverse-integer/]
    """
        neg = None
        ans = 0
        if x < 0:
            neg = True
            x *= -1
            
        while x > 0:
            y = x % 10
            x //= 10 
            
            temp = ans * 10 + y
            ans = temp
            
        if neg:
            ans *= -1
        
        if ans not in range(-2147483648, 2147483647):
            ans = 0
        
        return ans