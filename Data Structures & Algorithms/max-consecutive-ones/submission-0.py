class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = []
        counterr = 0
        for i in range (len(nums)):
            if nums[i] == 1:
                counterr +=1
            if nums[i] == 0:
                counter.append(counterr)
                counterr = 0

        counter.append(counterr)
        return max(counter)
        

