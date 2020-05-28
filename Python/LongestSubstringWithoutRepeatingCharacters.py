class Solution:
    """Solution to problem found at: [https://leetcode.com/problems/longest-substring-without-repeating-characters/]
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create set
        #itearate while letter not in set
        #iterate[+1:]
        
        if len(s) == 0: return 0
        
        if len(s) == 1: return 1

        longest = 0

        for start in range(len(s)):
            letters = set()
            index = start
            letter = s[index]
         
            while index < len(s):
                letter = s[index]
                if letter in letters:
                    break
                letters.add(letter)
                index += 1
          
            if len(letters) > longest: 
                longest = len(letters)
                print(letters)
           


        return longest


                
                
            
        
        
        