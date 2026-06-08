class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        right=1
        left=0
        strs=set([s[0]])
        result=1
        while right<len(s):
            if s[right] not in strs:
                strs.add(s[right])
                right+=1
                if result<right-left:
                    result=right-left
            else:
                strs.remove(s[left])
                left+=1
        return result
            



  
        