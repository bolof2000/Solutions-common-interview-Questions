class Solution:
    def isPalindrome(self, s):

        left =0
        right = len(s)
        while left <right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
    
        return True
        
