class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=1
        seen={s[0]:1}
        result=1
        while right<len(s):
            if s[right] not in seen:
                seen[s[right]]=1
            else:
                seen[s[right]]+=1
            if right-left+1-max(seen.values())>k:
                seen[s[left]]-=1
                left+=1
            result=max(result,right-left+1)
            right+=1
        return result
        