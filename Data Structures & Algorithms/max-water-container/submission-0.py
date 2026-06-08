class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right=len(heights)-1
        left=0
        result=0
        while left<right:
            length=right-left
            cal=length*min(heights[left],heights[right])
            if result<cal:
                result=cal
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return result

            