class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        result=[]
        for i in range(len(nums)):
            target=nums[i]
            left=i+1
            right=len(nums)-1
            while left<right:
                gap=nums[right]+nums[left]+target
                if gap==0 and [nums[i],nums[left],nums[right]] not in result:
                    result.append([nums[i],nums[left],nums[right]])
                    right-=1
                elif gap>0:
                    right-=1
                else:
                    left+=1
        return result

                
                    



