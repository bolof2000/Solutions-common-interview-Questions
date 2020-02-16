class Solution:
    def lengthOfLongestSubstring(self, s):

        dic = {}
        max_len =0
        window_start =0

        for i in range(len(s)):

            char = s[i]

            if char in dic and dic[char] >= window_start:
                window_start = dic[char]+1
            
            dic[char] = i
        
        max_length = max(max_length,i-window_start+1)

        return max_length

es