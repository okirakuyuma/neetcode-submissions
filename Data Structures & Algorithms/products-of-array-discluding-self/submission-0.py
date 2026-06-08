class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]
        right=[1]
        zero_count = 0
        result=[]
        for i in range(len(nums)):
            left.append(left[-1]*nums[i])
            right.append(right[-1]*nums[-(i+1)])

        right.reverse()   

        for i in range(len(nums)):
            result.append(left[i]*right[i+1])
        return result

            

