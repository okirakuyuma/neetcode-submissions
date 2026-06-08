class Solution:
    def findMin(self, nums: List[int]) -> int:
        right=len(nums)-1
        left=0
        mid=right//2
        while left<right:
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
            mid=(right+left)//2
        return nums[left]

        