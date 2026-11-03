class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lnth = len(nums)
        forward = [0] * lnth
        backward = [0] * lnth
        
        for i in range (len(nums)):
            if (i == 0):
                forward[i] = nums[i]
            else:
                forward[i] = forward[i-1] * nums[i]

        nums = nums[::-1]

        for i in range (len(nums)):
            if (i==0):
                backward[i] = nums[i]
            else:
                backward[i] = backward[i-1] * nums[i] 
        
        backward = backward[::-1]

        result = [0] * (len(nums))

        for i in range(len(result)):
            if (i == 0 ):
                result[i] = backward[i + 1]
            elif (i == (len(nums) - 1)):
                result[i] = forward[i-1]
            else:
                result[i] = forward[i-1] * backward[i+1]

        return result 


