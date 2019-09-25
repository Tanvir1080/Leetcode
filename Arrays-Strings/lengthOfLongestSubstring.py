class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) < 2):
            return len(s)
        
        seenChars = {}
        length = len(s)
        i = 0
        j = 0
        maxLength = 0
        
        while (i < length and j < length): 
            
            if not s[j] in seenChars:
                seenChars[s[j]] = 1
                j += 1
                maxLength = max(maxLength, j - i)
            else: 
                del seenChars[s[i]]
                i += 1
        
        return maxLength