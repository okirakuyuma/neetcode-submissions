class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right=[1]
        left=[1] 
        result=[]
        for i in range(len(nums)):
            right.append(right[-1]*nums[-i-1])
            left.append(left[-1]*nums[i])
        right.reverse()
        print(right)
        print(left)
        for n in range(len(right)-1):
            result.append(right[n+1]*left[n])
        return result

        
                  

